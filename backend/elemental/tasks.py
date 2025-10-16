import requests
import time
import os
import logging
from datetime import datetime, timezone
from decimal import Decimal
from elemental.models import Element, ElementPrice, PriceSource, Feedstock, FeedstockPrice
from celery import shared_task, current_task
import io
import pandas as pd
from decimal import Decimal
from django.db import transaction

# Celery worker log
logger = logging.getLogger(__name__)

# - Monthly World Bank Pink Sheet Ingestion -
PINK_SHEET_URL = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"

TARGETS = {
    "Iron ore": "Iron ore",
    "Potash": "Potassium chloride",
    "Phosphate Rock": "Phosphate rock",
    "LNG Japan": "LNG, Japan",
    "Copper": "Copper",
    "Nickel": "Nickel",
    "Zinc": "Zinc",
    "Lead": "Lead",
    "Tin": "Tin",
    "Silver": "Silver",
}

WB_FEEDSTOCK_MAP = {
    "Iron ore": 4,
    "Potash": 10,
    "Phosphate Rock": 12,
    "LNG Japan": 2,
}
WB_ELEMENT_MAP = {
    "Copper": 29,
    "Nickel": 28,
    "Zinc": 30,
    "Lead": 82,
    "Tin": 50,
    "Silver": 47,
}

UNITS = {
    "Iron ore": "USD/mt",
    "Potash": "USD/mt",
    "Phosphate Rock": "USD/mt",
    "LNG Japan": "USD/mmbtu",
    "Copper": "USD/mt",
    "Nickel": "USD/mt",
    "Zinc": "USD/mt",
    "Lead": "USD/mt",
    "Tin": "USD/mt",
    "Silver": "USD/toz",
}

@shared_task(
    bind=True,
    autoretry_for=(requests.RequestException,),
    retry_backoff=True,          # exponential backoff
    retry_jitter=True,
    retry_kwargs={"max_retries": 5},
)

def ingest_worldbank_pink_sheet(self):
    """
    Safe to run daily: fetch XLSX, detect latest month for target series, and upsert.
    Idempotent: if latest month already in DB for a series, skip it.
    """

    # Download file TODO use cached header and look for 304
    resp = requests.get(PINK_SHEET_URL, timeout=60)
    resp.raise_for_status()
    xls = pd.ExcelFile(io.BytesIO(resp.content))

    # Find the monthly sheet and select columns
    sheet_name = [s for s in xls.sheet_names if "Monthly" in s or "Prices" in s][0]
    df = pd.read_excel(xls, sheet_name=sheet_name, header=1)

    cols = ["Date"] + [v for v in TARGETS.values()]
    df = df[[c for c in cols if c in df.columns]].dropna(subset=["Date"])
    df["Date"] = pd.to_datetime(df["Date"]).dt.tz_localize(timezone.utc, nonexistent='shift_forward', ambiguous='NaT')
    latest_row = df.iloc[-1]
    latest_ts = latest_row["Date"].to_pydatetime()

    source, _ = PriceSource.objects.get_or_create(name="World Bank Pink Sheet")

    # 3) Upsert each series (idempotent)
    created, updated, skipped = 0, 0, 0
    with transaction.atomic():
        for disp_name, col in TARGETS.items():
            if col not in df.columns:
                skipped += 1
                continue
            price_val = latest_row[col]
            if pd.isna(price_val):
                skipped += 1
                continue

            currency = "USD"
            unit = UNITS.get(disp_name, "USD/unit")
            ts = latest_ts

            atomic = WB_ELEMENT_MAP.get(disp_name)
            feed = WB_FEEDSTOCK_MAP.get(disp_name)
            if atomic:
                element = Element.objects.get(atomic_number=atomic)
                obj, was_created = ElementPrice.objects.update_or_create(
                    element=element,
                    ts=ts,
                    defaults={
                        "price": Decimal(str(price_val)),
                        "currency": currency,
                        "unit": unit,
                        "source": source,
                    },
                )
                created += int(was_created)
                updated += int(not was_created)
            else:
                if feed:
                    feedstock = Feedstock.objects.get(feedstock_id=feed)
                    obj, was_created = FeedstockPrice.objects.update_or_create(
                        feedstock=feedstock,
                        ts=ts,
                        defaults={
                            "price": Decimal(str(price_val)),
                            "currency": currency,
                            "unit": unit,
                            "source": source,
                        },
                    )
                    created += int(was_created)
                    updated += int(not was_created)

    return {"created": created, "updated": updated, "skipped": skipped, "latest_ts": latest_ts.isoformat()}

# --- Configuration: APIninjas Real-time ---
API_KEY = os.environ.get("APININJAS_API_KEY") 
BASE_URL = "https://api.api-ninjas.com/v1/commodityprice" 
RETRY_DELAY = 600 
MAX_RETRIES = 5  

AN_ELEMENT_MAP = {
    "gold": 79,
    "platinum": 78,
    "palladium": 46,
    "aluminum": 13,
}

@shared_task(bind=True, max_retries=MAX_RETRIES)
def update_commodity_prices_task(self, countdown_seconds=3000):
    if not API_KEY:
        return

    elements_to_update = list(AN_ELEMENT_MAP.keys())
    total_elements = len(elements_to_update)
    start_time = time.time()
    
    logger.info(f"Starting price update for {total_elements} elements. Task ID: {self.request.id}")

    #PriceSource object creation
    SOURCE_NAME = "APINinjas CommodityPrice"
    try:
        source_obj = PriceSource.objects.get(name=SOURCE_NAME)
    except PriceSource.DoesNotExist:
        source_obj = PriceSource.objects.create(name=SOURCE_NAME)
    
    #Authentication headers
    headers = {
        'X-Api-Key': API_KEY 
    }

    for i, commodity_name in enumerate(elements_to_update):
        atomic_number = AN_ELEMENT_MAP[commodity_name]
        
        #Handle retries
        for attempt in range(self.max_retries + 1):
            try:
                logger.info(f"--- {i+1}/{total_elements} (Attempt {attempt+1}): Fetching {commodity_name.upper()} (No: {atomic_number}) ---")

                # API URL parameters
                params = {
                    'name': commodity_name,
                }
                
                # API Call with Header Authentication
                response = requests.get(BASE_URL, headers=headers, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()
                
                # --- Parse and Save Data ---
                
                # APIninjas returns list
                if isinstance(data, list):
                        if not data:
                            logger.warning(f"[WARN] Empty list for {commodity_name}.")
                            continue
                        item = data[0]
                elif isinstance(data, dict):
                        item = data
                else:
                        logger.warning(f"[WARN] Unexpected data type for {commodity_name}: {type(data)}")
                        continue
                price_value = item.get('price')
                currency_code = item.get('currency', 'USD')
                timestamp = datetime.now(timezone.utc) 

                if price_value is None:
                    logger.warning(f"[SKIP] Price data missing for {commodity_name} in the response.")
                    break

                else:
                #Save to Django ORM
                    ElementPrice.objects.create(
                        element=Element.objects.get(atomic_number=atomic_number),
                        ts=timestamp,
                        price=Decimal(str(price_value)),
                        currency=currency_code,
                        unit=f"{currency_code}/unit",
                        source=source_obj
                    )

                    logger.info(f"✅ Saved price: {price_value} {currency_code} for {commodity_name}")
                    break 
                    
                

            except requests.exceptions.Timeout as exc:
                #Handle Timeout or Connection Errors
                if attempt < self.max_retries:
                    logger.warning(f"❌ Timeout for {commodity_name}. Retrying in {RETRY_DELAY}s...")
                    time.sleep(RETRY_DELAY)
                    continue
                else:
                    logger.error(f"❌ Max retries reached for {commodity_name}. Skipping. Error: {exc}")
                    break
                    
            except requests.exceptions.HTTPError as exc:
                # Handle 4xx or 5xx errors
                status_code = exc.response.status_code
                if status_code in (429, 500, 502, 503): # Rate Limit or Server Errors
                    logger.warning(f"❌ {status_code} Error for {commodity_name}. Retrying in {RETRY_DELAY}s...")
                    # 'raise self.retry' is Celery-native; instead of sleep?
                    if attempt < self.max_retries:
                         time.sleep(RETRY_DELAY)
                         continue
                    else:
                        logger.error(f"❌ Max retries reached for {commodity_name}. Skipping. Error: {exc}")
                        break
                elif status_code == 403:
                    logger.error(f"❌ 403 Forbidden Error. Check APININJAS_API_KEY and subscription. Aborting loop.")
                    return
                else:
                    logger.error(f"❌ Unrecoverable HTTP Error for {commodity_name}: {exc}. Skipping.")
                    break
                    
            except Element.DoesNotExist:
                logger.error(f"[ERROR] Element with atomic_number {atomic_number} not found. Skipping.")
                break
                
            except Exception as e:
                logger.critical(f"[CRITICAL ERROR] Unexpected error for {commodity_name}: {e}. Skipping.")
                break
        time.sleep(90) # Sleep - rate limits

    # --- Task Conclusion and Rescheduling ---
    
    end_time = time.time()
    total_duration = round((end_time - start_time), 2)
    logger.info(f"--- Update Complete ---")
    logger.info(f"Total processing time: {total_duration} seconds.")

    logger.info(f"Rescheduling next run in {countdown_seconds} seconds.")
    update_commodity_prices_task.apply_async(countdown=countdown_seconds)


# how to call in shell
# update_commodity_prices_task.delay()
import pandas as pd
from datetime import datetime
from decimal import Decimal
from django.utils.timezone import now
from elemental.models import Element, ElementPrice, PriceSource

# Pink Sheet Excel
PINK_SHEET_URL = "https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx"


xls = pd.ExcelFile(PINK_SHEET_URL)
sheet_name = [s for s in xls.sheet_names if "Monthly" in s][0]  # e.g., "Monthly Prices"
df = pd.read_excel(xls, sheet_name=sheet_name, header=1)

# series we care about
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

cols = ["Date"] + list(TARGETS.values())
subset = df[cols].dropna(subset=["Date"])

# latest month
latest = subset.iloc[-1]
latest_date = pd.to_datetime(latest["Date"]).to_pydatetime()

# Create rows for model
records = []
for display_name, column_name in TARGETS.items():
    price = latest[column_name]
    if display_name == "LNG, Japan":
        # Convert from USD/MMBtu to USD/mt approx
        price = price * 52.22
    records.append({
        "name": display_name,
        "price": Decimal(str(price)),
        "ts": latest_date,
        "currency": "USD",
        "unit": "USD/mt"
    })

print("Latest World Bank Pink Sheet prices:")
for r in records:
    print(f"{r['name']:<16} {r['price']:>10} {r['unit']} ({r['ts'].date()})")

source, _ = PriceSource.objects.get_or_create(name="World Bank Pink Sheet")

for r in records:
    element = Element.objects.filter(name__iexact=r["name"]).first()
    if not element:
        print(f"⚠️ No Element record for {r['name']}")
        continue

    ElementPrice.objects.update_or_create(
        element=element,
        ts__date=r["ts"].date(),
        defaults={
            "ts": r["ts"],
            "price": r["price"],
            "currency": r["currency"],
            "unit": r["unit"],
            "source": source,
        },
    )

print("✅ World Bank monthly data upload complete.")
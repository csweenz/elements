 #Latest price for each element - pull timestamps, then prices, 
#TODO This will require a lot of work to pull abstractly
 #TODO use some kind of list instead of qs for caching, bandwidth

from django.db.models import OuterRef, Subquery, Max, F
from elemental.models import Element, ElementPrice

def elements_with_latest_price_list():
    latest_ts = ElementPrice.objects.filter(element=OuterRef('pk')).values('element').annotate(m=Max('ts')).values('m')[:1]
    # Fetch elements with their latest price
    qs = Element.objects.annotate(last_ts=Subquery(latest_ts)).filter(last_ts__isnull=False)
    latest_price = ElementPrice.objects.filter(element=OuterRef('pk'), ts=OuterRef('last_ts')).values('price')[:1]
    qs = qs.annotate(last_price=Subquery(latest_price)).values('atomic_number','symbol','last_ts','last_price')
    return list(qs)


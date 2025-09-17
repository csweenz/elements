from django.http import JsonResponse

def element_detail(request, symbol: str):
    # Simple test echo - use cache
    return JsonResponse({"ok": True, "symbol": symbol.upper(), "message": "pong"})

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.db.models import Max, OuterRef, Subquery, F
from elemental.models import Element, ElementPrice
from elemental.serializers import ElementSerializer, ElementPriceSerializer
from elemental.util.getters import elements_with_latest_price_list
from django.core.cache import cache

class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all().order_by("atomic_number")
    serializer_class = ElementSerializer
    permission_classes = [permissions.AllowAny]
    # friendly URLs like /api/elements/Cu/
    lookup_field = "symbol"
    lookup_value_regex = r"[A-Za-z]{1,3}"

    @action(detail=False, methods=["get"])
    def latest(self, request):
        cache_key = "elements_latest_price_v1"
        data = cache.get(cache_key)
        if data is None:
            qs = (elements_with_latest_price_list()
              .filter(last_ts__isnull=False)
              .order_by("atomic_number")
              .values("atomic_number", "symbol", "name", "last_ts", "last_price"))
            data = list(qs)
            cache.set(cache_key, data, timeout=600)  # 60s TTL
        return Response(data)

class ElementPriceViewSet(viewsets.ModelViewSet):
    queryset = ElementPrice.objects.select_related("element").all()
    serializer_class = ElementPriceSerializer
    permission_classes = [permissions.AllowAny]

    # Support filters: ?symbol=Cu or ?element=29 and ?start=YYYY-MM-DD&end=YYYY-MM-DD
    # Also ?latest=true to return latest price per element
    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params
        symbol = p.get("symbol")
        element = p.get("element")  # atomic_number
        start = p.get("start")
        end = p.get("end")
        latest = p.get("latest") in {"1", "true", "True"}

        if symbol:
            qs = qs.filter(element__symbol__iexact=symbol)
        if element:
            qs = qs.filter(element__atomic_number=element)
        if start:
            qs = qs.filter(ts__gte=start)
        if end:
            qs = qs.filter(ts__lt=end)

        if latest:
            # latest row per element
            latest_ts = ElementPrice.objects.filter(
                element=OuterRef("element")
            ).values("element").annotate(m=Max("ts")).values("m")[:1]
            qs = qs.annotate(last_ts=Subquery(latest_ts)).filter(ts=F("last_ts"))

        return qs.order_by("element__atomic_number", "ts")

@api_view(["GET"])
def healthz(_request):
    try:
        # Touch DB quickly
        Element.objects.only("atomic_number").first()
        db = True
    except Exception:
        db = False
    return Response({"status": "ok" if db else "degraded", "db": db})

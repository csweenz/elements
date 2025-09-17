from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElementViewSet, ElementPriceViewSet
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .healthz import healthz

router = DefaultRouter()
router.register(r"elements", ElementViewSet, basename="element")
router.register(r"element-prices", ElementPriceViewSet, basename="elementprice")

@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({"ok": True})

urlpatterns = [
    path("csrf/", csrf_token),
    path("", include(router.urls)),
    path('healthz', healthz),
]

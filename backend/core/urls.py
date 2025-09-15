# backend/core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ElementList,
    PriceSourceList,
    FeedstockList,
    ElementFeedstockWeightList,
    ElementPriceList,
    FeedstockPriceList,
)

from django.contrib import admin
from django.urls import path
from .healthz import healthz
from .views import element_detail



from django.http import JsonResponse
def hello(request):
    return JsonResponse({"message": "Testing API, testing 1 2 3"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthz', healthz),
    path("api/hello/", hello),
    path("api/elements/<str:symbol>", element_detail, name="element-detail"),
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'elements', ElementList)
router.register(r'pricesources', PriceSourceList)
router.register(r'feedstocks', FeedstockList)
router.register(r'elementfeedstockweights', ElementFeedstockWeightList)
router.register(r'elementprices', ElementPriceList)
router.register(r'feedstockprices', FeedstockPriceList)
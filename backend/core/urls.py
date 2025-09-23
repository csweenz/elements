# core/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from .views import healthz

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("elemental.urls")),
    re_path(r"^healthz/?$", healthz, name="healthz"),
]
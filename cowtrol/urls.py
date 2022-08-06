from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("farms.urls")),
    path("api/", include("areas.urls")),
    path("api/", include("animals.urls")),
    path("api/", include("movements.urls")),
]

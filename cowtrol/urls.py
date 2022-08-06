from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("farms.urls")),
    path("api/", include("areas.urls")),
    path("api/", include("animals.urls")),
    path("api/", include("movements.urls")),
]

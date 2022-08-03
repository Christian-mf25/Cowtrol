from django.urls import path
from farms.views import FarmView

urlpatterns = [
	path("farms/", FarmView.as_view()),
]
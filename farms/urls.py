from django.urls import path
from farms.views import FarmView, login

urlpatterns = [
	path("farms/", FarmView.as_view()),
	path("login/", login)
]
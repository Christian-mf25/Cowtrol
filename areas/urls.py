from django.urls import path

from areas.views import AreaView

urlpatterns = [
	path("areas/", AreaView.as_view()),
]
from django.urls import path

from movements.views import MovementView

urlpatterns = [
    path("movements/", MovementView.as_view()),
]

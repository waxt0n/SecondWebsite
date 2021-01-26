from django.urls import path

from . import views

urlpatterns = [
    path("", views.hall_of_fame, name="hall of fame"),
]

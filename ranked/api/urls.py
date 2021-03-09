from .views import EventsRudView, EventsAPIView

from django.urls import path

app_name = "api-ranked"


urlpatterns = [
    path('create/', RankedAPIView.as_view(), name="ranked-create"),
]

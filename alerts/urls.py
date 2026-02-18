from django.urls import path
from . import views

urlpatterns = [
    path("staff/", views.staff_alerts, name="staff_alerts"),
]

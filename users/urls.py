from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("dashboard/", views.dashboard_router, name="dashboard_router"),

    path("staff/", views.staff_dashboard, name="staff_dashboard"),
    path("supervisor/", views.supervisor_dashboard, name="supervisor_dashboard"),
    path("vendor/", views.vendor_dashboard, name="vendor_dashboard"),
]

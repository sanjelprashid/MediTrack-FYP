from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_requisition, name="create_requisition"),

    path("supervisor/", views.supervisor_requisitions, name="supervisor_requisitions"),
    path("approve/<int:pk>/", views.approve_requisition, name="approve_requisition"),
    path("reject/<int:pk>/", views.reject_requisition, name="reject_requisition"),

    path("vendor/", views.vendor_requisitions, name="vendor_requisitions"),
    path("fulfill/<int:pk>/", views.fulfill_requisition, name="fulfill_requisition"),


]

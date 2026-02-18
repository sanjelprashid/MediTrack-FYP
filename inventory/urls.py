from django.urls import path
from . import views

urlpatterns = [
    path("stock/", views.stock_list, name="stock_list"),
    path("consumption/", views.daily_consumption, name="daily_consumption"),

]

from django.contrib import admin
from .models import Stock, DailyConsumption

admin.site.register(Stock)
admin.site.register(DailyConsumption)

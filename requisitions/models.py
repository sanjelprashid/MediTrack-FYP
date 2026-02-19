from django.db import models
from inventory.models import Stock
from healthposts.models import HealthPost


class Requisition(models.Model):
    STATUS = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("FULFILLED", "Fulfilled"),
    ]

    facility = models.ForeignKey(HealthPost, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    quantity_requested = models.IntegerField()

    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock.medicine_name} - {self.quantity_requested}"

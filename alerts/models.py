from django.db import models


class Alert(models.Model):
    ALERT_TYPES = [
        ("LOW", "Low Stock"),
        ("OUT", "Out of Stock"),
    ]

    STATUS = [
        ("PENDING", "Pending"),
        ("RESOLVED", "Resolved"),
    ]

    stock = models.ForeignKey("inventory.Stock", on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    alert_status = models.CharField(max_length=20, choices=STATUS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stock.medicine_name} - {self.alert_type}"

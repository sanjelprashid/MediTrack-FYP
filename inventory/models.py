from django.db import models
from healthposts.models import HealthPost
from alerts.models import Alert



class Stock(models.Model):
    facility = models.ForeignKey(HealthPost, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=120)
    category = models.CharField(max_length=50)
    unit = models.CharField(max_length=30)

    quantity_available = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)

    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # create alert if stock low
        if self.quantity_available <= self.reorder_level:
            Alert.objects.get_or_create(
                stock=self,
                alert_status="PENDING",
                defaults={"alert_type": "LOW"}
            )

    def __str__(self):
        return f"{self.medicine_name} - {self.facility.facility_name}"


class DailyConsumption(models.Model):
    facility = models.ForeignKey(HealthPost, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    quantity_consumed = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    remarks = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.quantity_consumed > self.stock.quantity_available:
            raise ValueError("Not enough stock available")

        self.stock.quantity_available -= self.quantity_consumed
        self.stock.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stock.medicine_name} - {self.quantity_consumed}"

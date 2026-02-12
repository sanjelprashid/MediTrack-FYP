from django.db import models

class HealthPost(models.Model):
    facility_name = models.CharField(max_length=120)
    facility_type = models.CharField(max_length=50)
    district = models.CharField(max_length=80)
    province = models.CharField(max_length=80)

    def __str__(self):
        return self.facility_name

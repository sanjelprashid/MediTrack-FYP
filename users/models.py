from django.contrib.auth.models import AbstractUser
from django.db import models
from healthposts.models import HealthPost

class User(AbstractUser):
    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("STAFF", "Health Post Staff"),
        ("SUPERVISOR", "Supervisor"),
        ("VENDOR", "Vendor"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="STAFF")
    facility = models.ForeignKey(
        HealthPost,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

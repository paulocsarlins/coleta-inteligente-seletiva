from django.db import models
from django.conf import settings
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)
    companyType = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
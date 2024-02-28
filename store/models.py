from django.db import models
from core.models import *
# Create your models here.

class Customer(models.Model):
    store = models.ForeignKey(StoreUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

from django.conf import settings
from django.db import models

from products.models import Product

# Create your models here.
User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User,blank=True, null=True)
    products = models.ManyToManyField(Product,blank=True)
    total =  models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


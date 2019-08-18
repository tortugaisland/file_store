from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_time = models.DateTimeField('created time',auto_now_add=True)


class StoreProduct(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_time = models.DateTimeField('created time', auto_now_add=True)


class ProductFile(models.Model):
    store_product = models.ForeignKey(StoreProduct,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_time = models.DateTimeField('created time', auto_now_add=True)
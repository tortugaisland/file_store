from django.db import models
from stores.models import StoreProduct , ProductFile

class Star(models.Model):
    created_time = models.DateTimeField('created time', auto_now_add=True)

    class Meta:
        abstract = True


class StarProduct(Star):
    store_product = models.ForeignKey(StoreProduct,on_delete=models.PROTECT)


class StarFile(Star):
    product_file = models.ForeignKey(ProductFile, on_delete=models.PROTECT)




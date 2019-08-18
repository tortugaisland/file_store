from django.db import models
from stores.models import StoreProduct,ProductFile
from django.contrib.auth.models import User

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('created time', auto_now_add=True)

    class Meta:
        abstract = True


class CommentProduct(Comment):
    store_product = models.ForeignKey(StoreProduct,on_delete=models.PROTECT)


class CommentFile(Comment):
    product_file = models.ForeignKey(ProductFile,on_delete=models.PROTECT)




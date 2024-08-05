from django.contrib.auth.models import User
from django.db import models

from goods.models import Goods


# Create your models here.


#basket

class Cart_product(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()
    summa = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    class Meta:
        ordering = ['good']
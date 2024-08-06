from django.contrib.auth.models import User
from django.db import models

from goods.models import Good


# Create your models here.


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket')


class BasketGood(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='goods')
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='goods')
    quantity = models.IntegerField()
    summa = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    class Meta:
        ordering = ['good']
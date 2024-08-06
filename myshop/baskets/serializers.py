import datetime

from django.db.models import Sum
from rest_framework import serializers
from .models import Basket, BasketGood
from goods.models import Price
from goods.serializers import GoodsSerializer






class BasketGoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasketGood
        fields = ['good', 'quantity']

    def create(self, validated_data):
        """Метод для создания"""
        price = (Price.objects.all()
                 .filter(good=validated_data["good"],
                         date_price__lte=datetime.date.today())
                 .order_by('-date_price')
                 .values()[:1][0]['price'])
        validated_data["summa"] = price * validated_data["quantity"]
        validated_data["price"] = price

        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Метод для обновления"""
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.summa = instance.price * instance.quantity
        instance.save()
        return instance


class GoodsForBasketSerializer(serializers.ModelSerializer):
    good = GoodsSerializer()

    class Meta:
        model = BasketGood
        fields = ['good', 'quantity', 'price', 'summa']


class ItogField(serializers.Field):
    def to_representation(self, value):
        aggregate = BasketGood.objects.filter(basket_id=value).aggregate(summa=Sum("summa"), quantity= Sum("quantity"))
        return aggregate


class BasketSerializer(serializers.ModelSerializer):
    goods = GoodsForBasketSerializer(many=True)
    itog = ItogField(source='id')

    class Meta:
        model = Basket
        fields = ['id', 'itog', 'goods', ]



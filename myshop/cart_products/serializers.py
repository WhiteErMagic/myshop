import datetime
from rest_framework import serializers
from .models import Cart_product
from goods.models import Prices


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_product
        fields = ['good', 'quantity']

    def create(self, validated_data):
        """Метод для создания"""
        price = (Prices.objects.all()
                 .filter(good_id=validated_data["good"].id,
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

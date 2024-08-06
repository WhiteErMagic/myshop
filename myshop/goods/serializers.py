from rest_framework import serializers
from .models import Category, Good, GoodImage, Size, Price


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image',]


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'sub_categories',]

    @staticmethod
    def get_sub_categories(obj):
        return SubCategorySerializer(obj.subcategories, many=True, read_only=True).data


class ParentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', ]


class GoodsCategorySerializer(serializers.ModelSerializer):
    parent = ParentCategorySerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'parent', ]

    # def to_representation(self, instance):
    #     data = CategorySerializer(instance.parent)
    #     print(data)
    #     return data


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name_size', ]


class ImageGoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodImage
        fields = ['image', ]


class PricesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ['price', ]


class GoodsSerializer(serializers.ModelSerializer):
    images = ImageGoodSerializer(many=True)
    prices = PricesSerializer(many=True)
    category = GoodsCategorySerializer()

    class Meta:
        model = Good
        fields = ['id', 'name', 'slug', 'images', 'prices', 'category']

from rest_framework import serializers
from .models import Category, Goods, Images, Size, Prices


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image',]


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


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name_size', ]


class ImagesGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image', ]


class PricesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prices
        fields = ['price', ]


class GoodsSerializer(serializers.ModelSerializer):
    images = ImagesGoodsSerializer(many=True)
    prices = PricesSerializer(many=True)
    category_id = GoodsCategorySerializer()

    class Meta:
        model = Goods
        fields = ['id', 'name', 'slug', 'images', 'prices', 'category_id']


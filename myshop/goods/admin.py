from django.contrib import admin

from .models import Category, Good, Price, GoodImage, Size


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug', 'image',)
    prepopulated_fields = {'slug': ('name',)}


class ImagesInline(admin.TabularInline):
    model = GoodImage
    extra = 1


class PricesInline(admin.TabularInline):
    model = Price
    extra = 1


@admin.register(Good)
class GoodsAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        PricesInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Price)
class PricesAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
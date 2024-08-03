from django.contrib import admin

from .models import Category, Goods, Prices, Images, Size


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'name', 'slug', 'image',)
    prepopulated_fields = {'slug': ('name',)}


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


class PricesInline(admin.TabularInline):
    model = Prices
    extra = 1


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        PricesInline,
    ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
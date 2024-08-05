from django.db import models
from django.db.models import Max


# Create your models here.


class Category(models.Model):
    """
    Категории товаров
    """
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    Товары
    """
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='goods')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def __str__(self):
        return self.name


class PricesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(max_price=Max('price')).values('price')


class Prices(models.Model):
    """
    Цены товаров
    """
    good_id = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='prices', unique=False)
    date_price = models.DateTimeField(auto_created=True, verbose_name='Дата цены')
    price = models.DecimalField(max_digits=15, decimal_places=2)

    #objects = PricesManager()
    #first_object = PricesManager()

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        indexes = [
            models.Index(fields=['date_price', ]),
        ]
        ordering = ['good_id', 'date_price']

    def __str__(self):
        return f'{self.good_id} {self.date_price} {self.price} '


class Size(models.Model):
    """
    Список размеров картинок
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Размер картинки'
        verbose_name_plural = 'Размеры картинок'

    def __str__(self):
        return self.name


class Images(models.Model):
    """
    Картинки товаров
    """
    good_id = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(upload_to='goods_images', null=True, blank=True, verbose_name='Изображение')
    size = models.ForeignKey(Size, related_name='size_name', on_delete=models.PROTECT)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
# Generated by Django 5.0.7 on 2024-08-03 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_category_parent_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='goods',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterModelOptions(
            name='prices',
            options={'ordering': ['good_id', 'date_price'], 'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'Размер картинки', 'verbose_name_plural': 'Размеры картинок'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='goods.category'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='goods.category'),
        ),
        migrations.AlterField(
            model_name='prices',
            name='good_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='goods.goods'),
        ),
    ]

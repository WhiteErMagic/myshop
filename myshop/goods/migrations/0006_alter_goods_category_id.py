# Generated by Django 5.0.7 on 2024-08-03 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_rename_name_size_size_name_alter_images_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='goods.category'),
        ),
    ]

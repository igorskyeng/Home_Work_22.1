# Generated by Django 5.0.4 on 2024-04-29 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_product_created_at_alter_product_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 15, 33, 19, 3024), max_length=100, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 29, 15, 33, 19, 3024), max_length=100, verbose_name='Дата последнего изменения'),
        ),
    ]

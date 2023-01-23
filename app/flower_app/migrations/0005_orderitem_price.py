# Generated by Django 4.1.5 on 2023-01-20 14:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0004_order_payment_id_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(db_index=True, decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Общая стоимость товара'),
        ),
    ]

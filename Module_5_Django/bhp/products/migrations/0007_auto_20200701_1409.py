# Generated by Django 3.0.7 on 2020-07-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_refund_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

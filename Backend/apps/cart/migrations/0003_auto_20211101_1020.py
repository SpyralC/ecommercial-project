# Generated by Django 3.2.8 on 2021-11-01 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-31 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_alter_wishlist_cart_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='total_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='cart_id',
            new_name='wishlist_id',
        ),
    ]

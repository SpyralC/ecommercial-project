# Generated by Django 3.2.8 on 2021-11-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0005_auto_20211101_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='color',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='size',
        ),
    ]

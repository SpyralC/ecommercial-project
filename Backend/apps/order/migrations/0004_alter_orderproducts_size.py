# Generated by Django 3.2.8 on 2021-11-04 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20211103_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='size',
            field=models.CharField(default='M', max_length=50, verbose_name='size'),
        ),
    ]

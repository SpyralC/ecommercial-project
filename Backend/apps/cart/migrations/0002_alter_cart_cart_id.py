# Generated by Django 3.2.8 on 2021-10-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='cart id'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(verbose_name='date of birth'),
        ),
    ]

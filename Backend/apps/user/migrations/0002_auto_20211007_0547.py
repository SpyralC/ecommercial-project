# Generated by Django 3.2.8 on 2021-10-07 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='address',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='create time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='delete mark'),
        ),
        migrations.AddField(
            model_name='address',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
        migrations.AddField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='create time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='delete mark'),
        ),
        migrations.AddField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
    ]
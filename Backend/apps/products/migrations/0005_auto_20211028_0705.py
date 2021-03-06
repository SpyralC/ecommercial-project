# Generated by Django 3.2.8 on 2021-10-28 07:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_validdt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imgurl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='desc_image',
            field=models.TextField(null=True, verbose_name='desc_image'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.TextField(null=True, verbose_name='default_image'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.TextField(null=True, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=1024, verbose_name='product_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0, verbose_name='product_inventory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='product_name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='product_price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0, verbose_name='Quantity_sold'),
        ),
        migrations.AlterField(
            model_name='product',
            name='validdt',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='product_valid_date_and_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='validity',
            field=models.SmallIntegerField(choices=[(0, 'on shelves'), (1, 'off shelves')], default=0, verbose_name='product_validity'),
        ),
        migrations.CreateModel(
            name='SpecificationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete mark')),
                ('size', models.CharField(max_length=10, verbose_name='size')),
                ('color', models.CharField(max_length=10, verbose_name='color')),
                ('inventory', models.IntegerField(default=0, verbose_name='spec_prod_inventory')),
                ('prod_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='products.product', verbose_name='specification')),
            ],
            options={
                'verbose_name': 'specification_option',
                'verbose_name_plural': 'specification_option',
                'db_table': 'df_specification_option',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete mark')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='category_name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'product_category',
                'verbose_name_plural': 'product_category',
                'db_table': 'df_product_category',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cat1_spu', to='products.productcategory', verbose_name='primary_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cat2_spu', to='products.productcategory', verbose_name='second_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cat3_spu', to='products.productcategory', verbose_name='third_category'),
        ),
    ]

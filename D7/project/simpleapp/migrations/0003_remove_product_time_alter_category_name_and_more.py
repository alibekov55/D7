# Generated by Django 4.0.1 on 2022-03-01 09:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_product_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='time',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
    ]

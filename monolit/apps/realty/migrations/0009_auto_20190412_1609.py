# Generated by Django 2.2 on 2019-04-12 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0008_auto_20190412_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectsite',
            name='floor',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(100)], verbose_name='Этаж'),
        ),
    ]

# Generated by Django 2.2 on 2019-04-11 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0003_auto_20190411_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='object',
        ),
    ]

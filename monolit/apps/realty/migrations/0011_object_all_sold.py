# Generated by Django 2.2.2 on 2019-06-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0010_auto_20190624_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='all_sold',
            field=models.BooleanField(default=False, verbose_name='Все квартиры и помещения проданы'),
        ),
    ]
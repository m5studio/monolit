# Generated by Django 2.2 on 2019-04-11 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_auto_20190411_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object', verbose_name='Объект'),
        ),
    ]
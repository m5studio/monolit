# Generated by Django 2.2.1 on 2019-06-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_auto_20190531_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='genplan_svg',
            field=models.TextField(blank=True, null=True, verbose_name='SVG объекты на генплане'),
        ),
    ]

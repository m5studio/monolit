# Generated by Django 2.2.3 on 2019-07-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_auto_20190705_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='mortgage_military',
            field=models.BooleanField(default=False, help_text='Подходит ли данный объект под условия Военной ипотеки?', verbose_name='Военная ипотека'),
        ),
        migrations.AddField(
            model_name='object',
            name='mortgage_mother',
            field=models.BooleanField(default=False, help_text='Подходит ли данный объект под оплату Материнским капиталом?', verbose_name='Материнский капитал'),
        ),
    ]

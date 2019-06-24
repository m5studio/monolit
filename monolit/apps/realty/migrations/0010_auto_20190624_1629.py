# Generated by Django 2.2.2 on 2019-06-24 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0009_auto_20190614_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectsection',
            name='number',
            field=models.PositiveIntegerField(help_text='Номер секции числом', verbose_name='Номер секции'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.Object', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='price_per_square',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Стоимость одного квадратного метра', max_digits=10, null=True, verbose_name='Цена за м2 (руб.)'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Считается автоматически из Площади помещения * Цена за м2', max_digits=10, null=True, verbose_name='Общая стоимость (руб.)'),
        ),
    ]

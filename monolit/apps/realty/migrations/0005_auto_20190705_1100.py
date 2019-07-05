# Generated by Django 2.2.3 on 2019-07-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_auto_20190705_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectsite',
            name='ceiling_height',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Пример: 2.30 = 2 метра 30 см', max_digits=2, null=True, verbose_name='Высота потолка (м)'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='kitchen_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Площадь кухни'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='living_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Жилая площадь'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='price_per_square',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Стоимость одного квадратного метра', max_digits=6, null=True, verbose_name='Цена за м2 (руб.)'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Считается автоматически из Площади помещения * Цена за м2', max_digits=9, null=True, verbose_name='Общая стоимость (руб.)'),
        ),
        migrations.AlterField(
            model_name='objectsite',
            name='site_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Площадь помещения'),
        ),
    ]

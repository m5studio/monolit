# Generated by Django 3.0 on 2019-12-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_auto_20191205_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectcommercialinfotab',
            options={'verbose_name': 'Таб [Информация о коммерческом объекте]', 'verbose_name_plural': 'Табы [Информация о коммерческих объектах]'},
        ),
        migrations.AlterField(
            model_name='objectcommercialinfotab',
            name='icon_name',
            field=models.SlugField(blank=True, choices=[('about', 'Об объекте'), ('architecture', 'Архитектура'), ('land-improvement', 'Благоустройство'), ('location', 'Расположение'), ('communications', 'Коммуникации'), ('arrangement', 'Планировки'), ('parking', 'Паркинг'), ('servicing', 'Обслуживание')], max_length=100, null=True, verbose_name='Имя иконки (оно же заголовок таба)'),
        ),
    ]

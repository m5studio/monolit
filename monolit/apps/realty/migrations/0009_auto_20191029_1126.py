# Generated by Django 2.2.6 on 2019-10-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0008_auto_20191029_1034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Жилой Объект', 'verbose_name_plural': '1. Жилые Объекты'},
        ),
        migrations.AlterModelOptions(
            name='objectblock',
            options={'verbose_name': 'Блок Объекта', 'verbose_name_plural': '3. Блоки Объектов'},
        ),
        migrations.AlterModelOptions(
            name='objectcommercial',
            options={'verbose_name': 'Коммерческий Объект', 'verbose_name_plural': '2. Коммерческие Объекты'},
        ),
        migrations.AlterModelOptions(
            name='objectgallery',
            options={'verbose_name': 'Галерея Объекта', 'verbose_name_plural': 'Галереи Объектов'},
        ),
        migrations.AlterModelOptions(
            name='objectsection',
            options={'verbose_name': 'Секция Объекта', 'verbose_name_plural': '4. Секции Объектов'},
        ),
        migrations.AlterModelOptions(
            name='objectsite',
            options={'verbose_name': 'Жилое помещение', 'verbose_name_plural': '1.1 Жилые Помещения (Квартиры, Апартаменты)'},
        ),
        migrations.CreateModel(
            name='ObjectCommercialSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте', verbose_name='Активный')),
                ('special_offer', models.BooleanField(default=False, verbose_name='Спецпредложение')),
                ('crm_id', models.CharField(help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)', max_length=100, unique=True, verbose_name='CRM ID')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('object_commercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectCommercial', verbose_name='Коммерческий Объект')),
            ],
            options={
                'verbose_name': 'Коммерческое помещение',
                'verbose_name_plural': '2.1 Коммерческие Помещения (Офисы, Помещения свободного назначени)',
            },
        ),
    ]

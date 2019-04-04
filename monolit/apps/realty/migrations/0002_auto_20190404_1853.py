# Generated by Django 2.2 on 2019-04-04 15:53

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты (Жилые, Коммерческие)'},
        ),
        migrations.AddField(
            model_name='object',
            name='cetegory',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('living', 'Жилой'), ('commercial', 'Коммерческий')], default=1, help_text='Выберите категорию(и) объекта недвижимости', max_length=17, verbose_name='Категория объекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='city',
            field=models.CharField(choices=[('alushta', 'Алушта'), ('evpatoriya', 'Евпатория'), ('simferopol', 'Симферополь'), ('yalta', 'Ялта')], default=django.utils.timezone.now, max_length=100, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='object',
            name='crm_id',
            field=models.CharField(blank=True, help_text='ID объекта в 1C', max_length=100, null=True, verbose_name='CRM ID'),
        ),
        migrations.AddField(
            model_name='object',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='object',
            name='panoram',
            field=models.URLField(blank=True, help_text='e.g.: https://monolit360.com/files/main/index.html?s=pano1692', null=True, verbose_name='Cсылка на панораму'),
        ),
        migrations.AddField(
            model_name='object',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='object',
            name='webcam',
            field=models.URLField(blank=True, help_text='e.g.: https://rtsp.me/embed/3KASrTkG/', null=True, verbose_name='Cсылка на web-камеру'),
        ),
        migrations.AlterField(
            model_name='object',
            name='active',
            field=models.BooleanField(default=True, help_text='Опубликован на сайте', verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='object',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Строительство завершено'),
        ),
        migrations.AlterField(
            model_name='object',
            name='slug',
            field=models.SlugField(help_text='e.g.: object-url-path (max 100 chars)', max_length=100, verbose_name='URL адрес'),
        ),
    ]

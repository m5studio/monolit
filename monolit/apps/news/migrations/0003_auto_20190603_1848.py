# Generated by Django 2.2.1 on 2019-06-03 15:48

import apps.news.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190603_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.news.models.image_upload_path, verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.news.models.image_upload_path, verbose_name='Изображение'),
        ),
    ]
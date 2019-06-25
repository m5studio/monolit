# Generated by Django 2.2.1 on 2019-06-03 19:24

import apps.news.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190603_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='main_image_proc',
        ),
        migrations.AlterField(
            model_name='news',
            name='main_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.news.models.main_image_upload_path, verbose_name='Главное изображение'),
        ),
    ]
# Generated by Django 2.2 on 2019-04-26 14:51

import apps.realty.models.object_document
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_auto_20190426_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectdocument',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=apps.realty.models.object_document.file_upload_path, verbose_name='Файл'),
        ),
    ]
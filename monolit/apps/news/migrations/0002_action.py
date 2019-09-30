# Generated by Django 2.2.5 on 2019-09-30 06:38

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликована на сайте', verbose_name='Активная')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок акции')),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата начала акции')),
                ('date_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания акции')),
                ('date_test', models.DateField(default=django.utils.timezone.now, verbose_name='Дата test')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание акции')),
                ('partners_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок для партнеров')),
            ],
        ),
    ]

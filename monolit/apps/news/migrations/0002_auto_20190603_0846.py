# Generated by Django 2.2.1 on 2019-06-03 05:46

import apps.news.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_auto_20190531_1025'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='object',
            field=models.ManyToManyField(blank=True, help_text='Относится ли данная новость к Объекту(ам) недвижимости? Если нет, то оставьте пустым', to='realty.Object', verbose_name='Объект(ы)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(blank=True, to='news.NewsCategory', verbose_name='Категории новости'),
        ),
        migrations.AlterField(
            model_name='newscategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя категории'),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.news.models.image_upload_path, verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]

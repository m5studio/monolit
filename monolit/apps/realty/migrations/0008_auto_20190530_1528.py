# Generated by Django 2.2.1 on 2019-05-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0007_auto_20190530_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectvideo',
            name='video_url',
        ),
        migrations.AddField(
            model_name='objectvideo',
            name='video',
            field=models.CharField(blank=True, help_text='Укажите ссылку вида: https://www.youtube.com/watch?v=JbacFR_B-jw, https://youtu.be/JbacFR_B-jw или ID видео в YouTube, например: JbacFR_B-jw', max_length=100, null=True, verbose_name='Cсылка на видео в YouTube'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(blank=True, help_text='site meta &lt;title&gt;, max 100 chars', max_length=100, null=True, verbose_name='Site title')),
                ('site_description', models.TextField(blank=True, help_text='site meta description, max 150', max_length=150, null=True, verbose_name='Site description')),
                ('site_email', models.EmailField(blank=True, help_text='Основной email', max_length=255, null=True, verbose_name='Site Email')),
                ('site_phone', models.CharField(blank=True, help_text='Основной телефон, e.g.: +79784447711', max_length=50, null=True, verbose_name='Site Phone')),
                ('site_instagram', models.URLField(blank=True, help_text='e.g.: https://instagram.com/monolit.crimea/', max_length=255, null=True, verbose_name='Instagram')),
                ('site_facebook', models.URLField(blank=True, help_text='e.g.: https://facebook.com/monolit', max_length=255, null=True, verbose_name='Facebook')),
                ('site_vk', models.URLField(blank=True, help_text='e.g.: https://vk.com/monolit.crimea', max_length=255, null=True, verbose_name='VK (ВКонтакте)')),
                ('site_telegram', models.URLField(blank=True, help_text='e.g.: https://t.me/monolitstroit', max_length=255, null=True, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Основные настройки сайта',
                'verbose_name_plural': 'Основные настройки сайта',
            },
        ),
    ]
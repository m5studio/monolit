# Generated by Django 2.2.5 on 2019-09-30 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190930_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actions',
            old_name='image_for_card',
            new_name='image_card',
        ),
        migrations.RenameField(
            model_name='actions',
            old_name='image_for_detail',
            new_name='image_detail',
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0005_object_genplan_svg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectvideo',
            name='created',
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0003_auto_20190715_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='loan_payment_monthly',
        ),
    ]

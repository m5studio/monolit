# Generated by Django 2.2.6 on 2019-10-29 14:51

import apps.mortgage.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название банка')),
                ('logo', models.FileField(blank=True, null=True, upload_to=apps.mortgage.models.logo_upload_path, validators=[django.core.validators.FileExtensionValidator(['svg', 'png'])], verbose_name='Логотип банка (svg, png)')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='WayToBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('military', models.ManyToManyField(blank=True, help_text='Выберите Объекты подходящие под военную ипотеку', related_name='mortgage_object_military', to='realty.Object', verbose_name='Военная ипотека')),
                ('mother', models.ManyToManyField(blank=True, help_text='Выберите Объекты подходящие под материнский капитал', related_name='mortgage_object_mother', to='realty.Object', verbose_name='Материнский капитал')),
            ],
            options={
                'verbose_name': 'Способы покупки (Военная ипотека, Материнский капитал)',
                'verbose_name_plural': 'Способы покупки (Военная ипотека, Материнский капитал)',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название ипотечного кредита', max_length=255, verbose_name='Название программы')),
                ('first_payment_from', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='от')),
                ('first_payment_to', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='до')),
                ('loan_term_from', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='от')),
                ('loan_term_to', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)], verbose_name='до')),
                ('rate_from', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='от')),
                ('rate_to', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='до')),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Описание и дополнительные условия', null=True, verbose_name='Описание')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mortgage.Bank', verbose_name='Банк')),
                ('object', models.ManyToManyField(blank=True, help_text='Выберите Объекты подходящие под данную ипотечную программу', to='realty.Object', verbose_name='Объект(ы)')),
            ],
            options={
                'verbose_name': 'Ипотечная программа',
                'verbose_name_plural': 'Ипотечные программы',
            },
        ),
    ]

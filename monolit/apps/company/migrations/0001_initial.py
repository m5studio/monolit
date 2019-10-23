# Generated by Django 2.2.6 on 2019-10-23 11:12

import apps.company.models.certificate
import apps.company.models.history
import apps.company.models.job
import apps.company.models.management
import apps.company.models.partner
import apps.company.models.responsibility
import apps.company.models.structure
import apps.company.models.tender
import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название сертификата')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.certificate.image_upload_path, verbose_name='Фото сертификата')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.CreateModel(
            name='ContactsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы контактов')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('work_hours', models.TextField(blank=True, null=True, verbose_name='График работы')),
            ],
            options={
                'verbose_name': 'Группа контактов',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(default=2019, unique=True, validators=[django.core.validators.MinValueValidator(2005), django.core.validators.MaxValueValidator(2020)], verbose_name='Год')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.history.image_upload_path, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Блок (История компании)',
                'verbose_name_plural': 'История компании (Блоки)',
            },
        ),
        migrations.CreateModel(
            name='JobBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.job.image_upload_path, verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, help_text='Чем выше число, тем ниже объект в списке', verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Блок (Работа в компании)',
                'verbose_name_plural': 'Работа в компании (Блоки)',
            },
        ),
        migrations.CreateModel(
            name='JobVacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название должности')),
                ('experience', models.CharField(blank=True, help_text='Требования к опыту соискателя', max_length=255, null=True, verbose_name='Опыт')),
                ('duties', ckeditor.fields.RichTextField(blank=True, help_text='Описание должностных обязанностей', null=True, verbose_name='Обязанности')),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Требования к соискателю')),
                ('terms', ckeditor.fields.RichTextField(blank=True, help_text='Условия работы или преимущества компании', null=True, verbose_name='Условия')),
                ('salary', models.CharField(blank=True, help_text='Например: от 50 000 руб. или по результатам собеседования', max_length=255, null=True, verbose_name='Зарплата')),
                ('contacts', ckeditor.fields.RichTextField(blank=True, help_text='Контактные данные лица связанного с данной вакансией', null=True, verbose_name='Контакты')),
                ('order', models.PositiveIntegerField(default=0, help_text='Чем выше число, тем ниже объект в списке', verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Вакансия (Работа в компании)',
                'verbose_name_plural': 'Работа в компании (Вакансии)',
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.management.image_upload_path, verbose_name='Фото руководителя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Чем выше число, тем ниже объект в списке', null=True, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Менеджмент (Рукововодство)',
                'verbose_name_plural': 'Менеджмент (Руководители)',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='URL сайта партнера')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.partner.image_upload_path, verbose_name='Логотип партнера')),
                ('order', models.PositiveIntegerField(default=0, help_text='Чем выше число, тем ниже объект в списке', verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Блок (Партнер)',
                'verbose_name_plural': 'Партнеры (Блоки)',
            },
        ),
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.responsibility.image_upload_path, verbose_name='Изображение')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('order', models.PositiveIntegerField(default=0, help_text='Чем выше число, тем ниже объект в списке', verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Блок Социальной ответственности',
                'verbose_name_plural': 'Социальная ответственность (Блоки)',
            },
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='URL сайта')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.company.models.structure.image_upload_path, verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, help_text='Чем выше число, тем ниже объект в списке', verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Блок (Структура компании)',
                'verbose_name_plural': 'Структура компании (Блоки)',
            },
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Является ли данный Тендер активным?', verbose_name='Активный')),
                ('title', models.CharField(max_length=255, verbose_name='Название тендера')),
                ('category', models.CharField(choices=[('construction', 'Строительство'), ('materials', 'Материалы'), ('equipment', 'Оборудование'), ('projecting', 'Проектирование'), ('other', 'Другое')], max_length=100, verbose_name='Категория тендера')),
                ('duties', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Обязанности')),
                ('requirements', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Требования')),
                ('contacts', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контакты')),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Срок проведения (начало)')),
                ('date_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Срок проведения (конец)')),
            ],
            options={
                'verbose_name': 'Тендер',
                'verbose_name_plural': 'Тендеры',
            },
        ),
        migrations.CreateModel(
            name='TenderFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Является ли данный вопрос-ответ активным?', verbose_name='Активный')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Чем выше число, тем ниже вопрос в списке', null=True, verbose_name='Порядок')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Вопрос-ответ по Тендерам',
                'verbose_name_plural': 'Тендеры (Вопросы-ответы)',
            },
        ),
        migrations.CreateModel(
            name='TenderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название документа')),
                ('file', models.FileField(blank=True, null=True, upload_to=apps.company.models.tender.file_upload_path, verbose_name='Файл')),
                ('tender', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='company.Tender')),
            ],
            options={
                'verbose_name': 'Тендер (Файл)',
                'verbose_name_plural': 'Тендеры (Файлы)',
            },
        ),
        migrations.CreateModel(
            name='ContactsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_description', models.CharField(max_length=255, verbose_name='Описание контакта')),
                ('сontact_type', models.CharField(choices=[('phone', 'Телефон'), ('email', 'Email')], max_length=100, verbose_name='Тип контакта')),
                ('contact', models.CharField(help_text='Заполняется номером телефона или email. Например: +79270004411 или mail@monolit.net', max_length=255, verbose_name='Контакт')),
                ('сontacts_group', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='company.ContactsGroup')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]

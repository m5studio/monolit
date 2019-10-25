# Generated by Django 2.2.6 on 2019-10-25 11:39

import apps.realty.models.object
import apps.realty.models.object_document
import apps.realty.models.object_file
import apps.realty.models.object_gallery
import apps.realty.models.object_info_tab
import apps.realty.models.object_site
import ckeditor.fields
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте', verbose_name='Активный')),
                ('completed', models.BooleanField(default=False, verbose_name='Строительство завершено')),
                ('all_sold', models.BooleanField(default=False, help_text='Все квартиры и помещения проданы', verbose_name='Все помещения проданы')),
                ('partnership', models.BooleanField(default=False, help_text='Участвует ли данный объект в партнерской программе?', verbose_name='Партнерская программа')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Чем выше число, тем ниже объект в списке', null=True, verbose_name='Порядок')),
                ('crm_id', models.CharField(help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)', max_length=100, unique=True, verbose_name='CRM ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Название объекта')),
                ('slug', models.SlugField(help_text='e.g.: status-house (max 100 chars), получим https://monolit.site/objects/status-house/', max_length=100, unique=True, verbose_name='URL адрес')),
                ('address', models.CharField(blank=True, help_text='Город, улица, номер дома (для завершенных/построенных объектов)', max_length=255, null=True, verbose_name='Адрес')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('genplan', models.ImageField(blank=True, help_text='Изображение с генпланом', null=True, upload_to=apps.realty.models.object.genplan_upload_path, verbose_name='Генплан')),
                ('genplan_svg', models.TextField(blank=True, null=True, verbose_name='SVG объекты на генплане')),
                ('webcam', models.URLField(blank=True, help_text='e.g.: https://rtsp.me/embed/3KASrTkG/', null=True, verbose_name='Cсылка на web-камеру')),
                ('panoram', models.URLField(blank=True, help_text='e.g.: https://monolit360.com/files/main/index.html?s=pano1692', null=True, verbose_name='Cсылка на панораму')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=apps.realty.models.object.image_upload_path, verbose_name='Главное изображение')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Жилой Объект',
                'verbose_name_plural': 'Объекты (Жилые)',
            },
        ),
        migrations.CreateModel(
            name='ObjectBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер блока или его название')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object', verbose_name='Жилой Объект')),
            ],
            options={
                'verbose_name': 'Блок Объекта',
                'verbose_name_plural': 'Объект Блоки',
            },
        ),
        migrations.CreateModel(
            name='ObjectBuildingTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Тип Здания')),
                ('slug', models.CharField(blank=True, help_text='e.g.: если название "Монолитно-каркасный", то здесь заполняется как "monolith-frame"', max_length=100, null=True, unique=True, verbose_name='Тип Здания (eng)')),
            ],
            options={
                'verbose_name': 'Тип Здания',
                'verbose_name_plural': 'Типы Зданий',
            },
        ),
        migrations.CreateModel(
            name='ObjectDocumentAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Пример: Иванов В.А.', max_length=255, unique=True, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор документа',
                'verbose_name_plural': 'Авторы документов',
            },
        ),
        migrations.CreateModel(
            name='ObjectGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='Чем выше число, тем ниже объект в списке', null=True, verbose_name='Порядок')),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок галереи')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object', verbose_name='Жилой Объект')),
            ],
            options={
                'verbose_name': 'Галерея Объекта',
                'verbose_name_plural': 'Фото Галереи Объектов',
            },
        ),
        migrations.CreateModel(
            name='ObjectSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название секции и её номер. Например: Секция 1', max_length=255, verbose_name='Название секции')),
                ('year_of_construction', models.PositiveIntegerField(blank=True, default=2019, help_text='Допустимые значения от 2019 до 2100', null=True, validators=[django.core.validators.MinValueValidator(2019), django.core.validators.MaxValueValidator(2100)], verbose_name='Год сдачи')),
                ('floor_first', models.IntegerField(blank=True, help_text='мин. этаж: -5', null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(0)], verbose_name='Этаж Первый')),
                ('floor_last', models.IntegerField(blank=True, help_text='макс. этаж: 100', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Этаж Последний')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object', verbose_name='Жилой Объект')),
                ('object_block', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectBlock', verbose_name='Блок Объекта')),
            ],
            options={
                'verbose_name': 'Секция Объекта',
                'verbose_name_plural': 'Объекты (Секции)',
            },
        ),
        migrations.CreateModel(
            name='ObjectSiteWindowsView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Вид из окон')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название Типа объекта')),
                ('name_declension', models.CharField(blank=True, help_text='Пример: "Жилой квартал" указать "Жилом квартале", "Курортный комплекс" указать "Курортном комплексе"', max_length=255, null=True, verbose_name='Склонение')),
                ('name_abbreviation', models.CharField(blank=True, help_text='Пример: "Жилой квартал" указать "ЖК" или иные сокращения: ТРЦ, БЦ, КК', max_length=255, null=True, verbose_name='Сокращение')),
                ('slug', models.CharField(blank=True, help_text='e.g.: если название "Жилой квартал", то здесь заполняется как "living-quarter"', max_length=100, null=True, unique=True, verbose_name='Название Типа объекта (eng)')),
            ],
            options={
                'verbose_name': 'Тип Объекта',
                'verbose_name_plural': 'Типы Объектов',
            },
        ),
        migrations.CreateModel(
            name='ObjectVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(blank=True, help_text='Укажите ссылки вида: https://www.youtube.com/watch?v=JbacFR_B-jw или https://youtu.be/JbacFR_B-jw Либо ID видео в YouTube, например: JbacFR_B-jw', max_length=100, null=True, verbose_name='ID видео в YouTube')),
                ('object', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='realty.Object')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='ObjectSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте', verbose_name='Активный')),
                ('special_offer', models.BooleanField(default=False, verbose_name='Спецпредложение')),
                ('site_type', models.CharField(choices=[('flat', 'Квартира'), ('apartments', 'Апартаменты')], max_length=100, verbose_name='Тип помещения')),
                ('crm_id', models.CharField(help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)', max_length=100, unique=True, verbose_name='CRM ID')),
                ('floor', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-5), django.core.validators.MaxValueValidator(100)], verbose_name='Этаж')),
                ('site_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер квартиры или помещения')),
                ('price_per_square', models.DecimalField(blank=True, decimal_places=2, help_text='Стоимость одного квадратного метра', max_digits=8, null=True, verbose_name='Цена за м2 (руб.)')),
                ('price_total', models.DecimalField(blank=True, decimal_places=2, help_text='Считается автоматически из Площади помещения * Цена за м2', max_digits=11, null=True, verbose_name='Общая стоимость (руб.)')),
                ('rooms_qty', models.CharField(blank=True, choices=[('0', 'Студия'), ('1', '1 комнатная'), ('2', '2 комнатная'), ('3', '3 комнатная'), ('4', '4 комнатная'), ('5', '5 комнатная')], max_length=100, null=True, verbose_name='Количество комнат в помещении')),
                ('site_area', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Площадь помещения')),
                ('living_area', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Жилая площадь')),
                ('kitchen_area', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Площадь кухни')),
                ('ceiling_height', models.DecimalField(blank=True, decimal_places=2, help_text='Пример: 2.30 = 2 метра 30 см', max_digits=4, null=True, verbose_name='Высота потолка (м)')),
                ('two_levels', models.BooleanField(default=False, help_text='Квартира с полноценным 2-м этажом', verbose_name='Двухуровневая квартира')),
                ('entresol', models.BooleanField(default=False, help_text='Наличие в квартире этажа-антресоли', verbose_name='Антресоль')),
                ('wardrobe', models.BooleanField(default=False, help_text='Помещение для гардеробной или кладовой', verbose_name='Гардеробная')),
                ('finish_type', models.CharField(blank=True, choices=[('0', 'Без отделки'), ('1', 'Черновая'), ('2', 'Чистовая')], max_length=100, null=True, verbose_name='Отделка')),
                ('image_planning', models.ImageField(blank=True, null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Планировка')),
                ('image_planning3d', models.ImageField(blank=True, null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Планировка 3D')),
                ('image_floor', models.ImageField(blank=True, help_text='Планировка квартиры на этаже', null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Квартира на этаже')),
                ('image_section', models.ImageField(blank=True, help_text='Выделенный этаж в секции объекта', null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Этаж в секции')),
                ('image_section_in_object', models.ImageField(blank=True, help_text='Выделенная секция в доме', null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Секция в доме')),
                ('image_genplan', models.ImageField(blank=True, help_text='Выделенный дом на генплане', null=True, upload_to=apps.realty.models.object_site.image_upload_path, verbose_name='Дом на генплане')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object', verbose_name='Жилой Объект')),
                ('object_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.ObjectBlock', verbose_name='Блок Объекта')),
                ('object_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.ObjectSection', verbose_name='Секция Объекта')),
                ('window_view', models.ManyToManyField(blank=True, to='realty.ObjectSiteWindowsView', verbose_name='Вид из окон')),
            ],
            options={
                'verbose_name': 'Жилое помещение',
                'verbose_name_plural': 'Помещения (Жилые)',
            },
        ),
        migrations.CreateModel(
            name='ObjectInfoTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.SlugField(blank=True, choices=[('about', 'Об объекте'), ('architecture', 'Архитектура'), ('land-improvement', 'Благоустройство'), ('location', 'Расположение'), ('communications', 'Коммуникации'), ('arrangement', 'Планировки'), ('storage-room', 'Кладовые'), ('parking', 'Паркинг')], max_length=100, null=True, verbose_name='Имя иконки (оно же заголовок таба)')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.realty.models.object_info_tab.image_upload_path, verbose_name='Изображение')),
                ('object', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='realty.Object')),
            ],
            options={
                'verbose_name': 'Таб [Информация об объекте]',
                'verbose_name_plural': 'Табы [Информация об объекте: Об объекте, Архитектура, Благоустройство, Расположение, Коммуникации, Планировки, Кладовые...]',
            },
        ),
        migrations.CreateModel(
            name='ObjectGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.realty.models.object_gallery.image_upload_path, verbose_name='Изображение')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectGallery', verbose_name='Галерея')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='ObjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('info_booklet', 'Информационный буклет'), ('object_genplan', 'Генплан объекта недвижимости'), ('commercial_offer', 'Коммерческое предложение')], max_length=100, null=True, verbose_name='Название документа')),
                ('file', models.FileField(blank=True, null=True, upload_to=apps.realty.models.object_file.file_upload_path, verbose_name='Файл')),
                ('object', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='realty.Object')),
            ],
            options={
                'verbose_name': 'Файл Объекта',
                'verbose_name_plural': 'Файлы Объектов (Информационный буклет, Генплан объекта недвижимости, Коммерческое предложение)',
            },
        ),
        migrations.CreateModel(
            name='ObjectElevator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevator_type', models.CharField(blank=True, choices=[('passenger_lift', 'Пассажирский лифт'), ('cargo_lift', 'Грузовой лифт')], max_length=100, null=True, verbose_name='Тип лифта')),
                ('elevator_qty', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Количество лифтов')),
                ('object_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectSection', verbose_name='Секция Объекта')),
            ],
            options={
                'verbose_name': 'Лифт Объекта',
                'verbose_name_plural': 'Лифты Объекта',
            },
        ),
        migrations.CreateModel(
            name='ObjectDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название документа')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('file', models.FileField(blank=True, null=True, upload_to=apps.realty.models.object_document.file_upload_path, verbose_name='Файл')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.ObjectDocumentAuthor', verbose_name='Автор')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realty.Object')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='ObjectCommercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.Object', verbose_name='Жилой Объект')),
                ('object_blocks', models.ManyToManyField(blank=True, to='realty.ObjectBlock', verbose_name='Блоки Объекта')),
                ('object_sections', models.ManyToManyField(blank=True, to='realty.ObjectSection', verbose_name='Секции Объекта')),
            ],
            options={
                'verbose_name': 'Коммерческий Объект',
                'verbose_name_plural': 'Объекты (Коммерческие)',
            },
        ),
        migrations.CreateModel(
            name='ObjectBathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathroom_type', models.CharField(blank=True, choices=[('0', 'Совмещенный'), ('1', 'Раздельный'), ('2', 'На этаже')], max_length=100, null=True, verbose_name='Тип санузла')),
                ('bathroom_qty', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Количество санузлов')),
                ('object_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectSite')),
            ],
            options={
                'verbose_name': 'Санузел',
                'verbose_name_plural': 'Санузлы',
            },
        ),
        migrations.CreateModel(
            name='ObjectBalcony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balcony_type', models.CharField(blank=True, choices=[('balcony', 'Балкон'), ('loggia', 'Лоджия'), ('terrace', 'Терраса'), ('patio', 'Патио'), ('french_balcony', 'Французский балкон'), ('bay_window', 'Эркер')], max_length=100, null=True, verbose_name='Тип балкона')),
                ('balcony_qty', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Количество балконов')),
                ('object_site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realty.ObjectSite')),
            ],
            options={
                'verbose_name': 'Балкон',
                'verbose_name_plural': 'Балконы в помещении',
            },
        ),
        migrations.AddField(
            model_name='object',
            name='building_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.ObjectBuildingTypes', verbose_name='Тип Здания'),
        ),
        migrations.AddField(
            model_name='object',
            name='object_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='realty.ObjectTypes', verbose_name='Тип Объекта'),
        ),
    ]

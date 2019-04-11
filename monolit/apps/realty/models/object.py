from django.db import models
from django.urls import reverse

from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from location_field.models.plain import PlainLocationField


class Object(models.Model):
    CATEGORIES = (
        ('living', 'Жилой'),
        ('commercial', 'Коммерческий'),
    )

    OBJECT_TYPES = (
        ('business_center', 'Бизнес центр'),
        ('city', 'Город'),
        ('living_house', 'Жилой дом'),
        ('living_quarter', 'Жилой квартал'),
        ('living_complex', 'Жилой комплекс'),
        ('resort_complex', 'Курортный комплекс'),
        ('multipurposes_complex', 'Многофункциональный комплекс'),
        ('family_quarter', 'Семейный квартал'),
        ('business_and_retail_center', 'Торгово-офисный центр'),
        ('mall', 'Торговый центр'),
    )

    CITIES = (
        ('alushta', 'Алушта'),
        ('evpatoriya', 'Евпатория'),
        ('simferopol', 'Симферополь'),
        ('yalta', 'Ялта'),
    )

    active       = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    completed    = models.BooleanField('Строительство завершено', default=False)
    order        = models.PositiveIntegerField('Порядок', default=0, blank=True, null=True, help_text='Чем выше число, тем ниже объект в списке')
    crm_id       = models.CharField('CRM ID', max_length=100, blank=True, null=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    name         = models.CharField('Название объекта', max_length=255, db_index=True)
    slug         = models.SlugField('URL адрес', max_length=100, help_text='e.g.: status-house (max 100 chars), получим https://monolit.site/objects/status-house/')
    category     = MultiSelectField('Категория объекта',
                                   choices=CATEGORIES,
                                   # default=[CATEGORIES[0][0], CATEGORIES[1][0]],
                                   blank=True, null=True,
                                   help_text='Выберите категорию(и) объекта недвижимости')
    object_type  = models.CharField('Тип Объекта', max_length=100, choices=OBJECT_TYPES, blank=True, null=True)
    city         = models.CharField('Город', max_length=100, choices=CITIES, blank=True, null=True)
    address      = models.CharField('Адрес', max_length=255, blank=True, null=True, help_text='Город, улица, номер дома (для завершенных/построенных объектов)')
    location     = PlainLocationField(verbose_name='Локация', blank=True, null=True, based_fields=['address'], default='44.952117,34.10241700000006', help_text='Географические координаты - широта и долгота')
    description  = RichTextField('Описание', blank=True, null=True)
    genplan      = models.ImageField('Генплан', upload_to='realty/objects/genplan/', blank=True, null=True, help_text='Изображение с генпланом')
    has_military = models.BooleanField('Военная ипотека', default=False, help_text='Подходит ли данный объект для военной ипотеки')
    webcam       = models.URLField('Cсылка на web-камеру', blank=True, null=True, help_text='e.g.: https://rtsp.me/embed/3KASrTkG/')
    panoram      = models.URLField('Cсылка на панораму', blank=True, null=True, help_text='e.g.: https://monolit360.com/files/main/index.html?s=pano1692')
    created      = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated      = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    # galleries    = models.ManyToManyField(Gallery, verbose_name='Галереи Объекта', help_text='Связанные с Объектом галереи изображений')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('object-detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты (Жилые, Коммерческие)'

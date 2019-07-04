from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.urls import reverse
from django.utils.html import mark_safe

from ckeditor.fields import RichTextField
from location_field.models.plain import PlainLocationField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from apps.core.classes.clean_media import CleanMedia
from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.image_optimizer import ImageOptimizer


class ObjectCategory(models.Model):
    name = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.name


def genplan_upload_path(instance, filename):
    object_name = instance.crm_id
    filename = FileProcessing(filename)
    filename = filename.newFileNameGenplan()
    return 'objects/{object_name}/{filename}'.format(object_name=object_name, filename=filename)

def image_upload_path(instance, filename):
    object_crm_id = instance.crm_id
    filename = FileProcessing(filename)
    filename = filename.newFileNameGenerated()
    return 'objects/{object_crm_id}/images/{filename}'.format(object_crm_id=object_crm_id, filename=filename)

class Object(models.Model):
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

    BUILDING_TYPES = (
        ('monolith', 'Монолитный'),
        ('monolith_frame', 'Монолитно-каркасный'),
        ('panel', 'Панельный'),
    )

    active        = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    completed     = models.BooleanField('Строительство завершено', default=False)
    all_sold      = models.BooleanField('Все помещения проданы', default=False, help_text='Все квартиры и помещения проданы')
    order         = models.PositiveIntegerField('Порядок', default=0, blank=True, null=True, help_text='Чем выше число, тем ниже объект в списке')
    crm_id        = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    name          = models.CharField('Название объекта', unique=True, max_length=255, db_index=True)
    slug          = models.SlugField('URL адрес', max_length=100, unique=True, help_text='e.g.: status-house (max 100 chars), получим https://monolit.site/objects/status-house/')
    category      = models.ManyToManyField(ObjectCategory,
                                           verbose_name='Категория объекта',
                                           help_text='Выберите категорию(и) объекта недвижимости')
    object_type   = models.CharField('Тип Объекта', max_length=100, choices=OBJECT_TYPES, blank=True, null=True)
    building_type = models.CharField('Тип Здания', max_length=100, choices=BUILDING_TYPES, blank=True, null=True)
    city          = models.CharField('Город', max_length=100, choices=CITIES, blank=True, null=True)
    address       = models.CharField('Адрес', max_length=255, blank=True, null=True, help_text='Город, улица, номер дома (для завершенных/построенных объектов)')
    location      = PlainLocationField(verbose_name='Локация',
                                       blank=True, null=True,
                                       based_fields=['address'],
                                       default='44.952117,34.10241700000006',
                                       help_text='Географические координаты: широта, долгота')
    description   = RichTextField('Описание', blank=True, null=True)
    genplan       = models.ImageField('Генплан',
                                      upload_to=genplan_upload_path,
                                      blank=True, null=True,
                                      help_text='Изображение с генпланом')
    genplan_svg   = models.TextField('SVG объекты на генплане', blank=True, null=True)
    # has_military  = models.BooleanField('Военная ипотека', default=False, help_text='Подходит ли данный объект для военной ипотеки')
    # has_mother    = models.BooleanField('Материнский капитал', default=False, help_text='Подходит ли данный объект под оплату мат.капиталом')

    webcam        = models.URLField('Cсылка на web-камеру', blank=True, null=True, help_text='e.g.: https://rtsp.me/embed/3KASrTkG/')
    panoram       = models.URLField('Cсылка на панораму', blank=True, null=True, help_text='e.g.: https://monolit360.com/files/main/index.html?s=pano1692')

    main_image    = models.ImageField('Главное изображение',
                                      upload_to=image_upload_path,
                                      blank=True, null=True)
    main_image_thumb = ImageSpecField(source='main_image',
                                        processors=[ResizeToFill(512, 386)],
                                        format = 'JPEG',
                                        options={'quality': 70})

    updated       = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    # Thumbnails for admin
    def genplan_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.genplan.url))
    genplan_thumb.short_description = 'Генплан (thumbnail)'

    def main_image_thumb_admin(self):
        return mark_safe('<img src="{}" alt="" style="width: 40%; height: auto;" />'.format(self.main_image.url))
    main_image_thumb_admin.short_description = 'Главное изображение (thumbnail)'
    # END Thumbnails for admin

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('object:detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты (Жилые, Коммерческие)'


@receiver(post_save, sender=Object)
def genplan_image_optimization(sender, instance, created, **kwargs):
    if instance.genplan:
        image = ImageOptimizer(instance.genplan.path)
        image.optimizeAndSaveImg()
    if instance.main_image:
        image = ImageOptimizer(instance.main_image.path)
        image.optimizeAndSaveImg()
    # Delete empty dirs in /media/
    cleanMedia = CleanMedia()
    cleanMedia.deleteEmptyDirsRecusive()


@receiver(post_delete, sender=Object)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete imagekit chache file
    cleanMedia.cleanImagekitCacheImage(instance.main_image_thumb)
    # Delete empty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

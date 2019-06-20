from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from apps.core.classes.clean_media import CleanMedia
from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object import Object
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection


class ObjectSiteWindowsView(models.Model):
    name = models.CharField('Вид из окон', max_length=255)

    def __str__(self):
        return self.name


def image_upload_path(instance, filename):
    object_crm_id = instance.object.crm_id
    site_crm_id = instance.crm_id
    filename = FileProcessing(filename)
    filename = filename.newFileNameGenerated()
    return 'objects/{object_crm_id}/sites/{site_crm_id}/{filename}'.format(object_crm_id=object_crm_id, site_crm_id=site_crm_id, filename=filename)

class ObjectSite(models.Model):
    SITE_TYPES = (
        ('flat', 'Квартира'),
        ('apartments', 'Апартаменты'),
        ('commercial', 'Коммерческое помещение'),
    )

    ROOMS_QTY = (
        ('0', 'Студия'),
        ('1', '1 комнатная'),
        ('2', '2 комнатная'),
        ('3', '3 комнатная'),
        ('4', '4 комнатная'),
        ('5', '5 комнатная'),
    )

    FINISHING_TYPES = (
        ('0', 'Без отделки'),
        ('1', 'Черновая'),
        ('2', 'Чистовая'),
    )

    active                  = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    special_offer           = models.BooleanField('Спецпредложение', default=False)

    object                  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.SET_NULL, blank=True, null=True)
    site_type               = models.CharField('Тип помещения', max_length=100, choices=SITE_TYPES)
    object_block            = models.ForeignKey(ObjectBlock, verbose_name='Блок Объекта', on_delete=models.SET_NULL, blank=True, null=True)
    object_section          = models.ForeignKey(ObjectSection, verbose_name='Секция Объекта', on_delete=models.SET_NULL, blank=True, null=True)

    crm_id                  = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    floor                   = models.IntegerField('Этаж', validators=[MinValueValidator(-5), MaxValueValidator(100)], blank=True, null=True)
    site_number             = models.CharField('Номер квартиры или помещения', max_length=100, blank=True, null=True)
    price_per_square        = models.DecimalField('Цена за м2 (руб.)', max_digits=20, decimal_places=2, blank=True, null=True, help_text='Стоимость одного квадратного метра')
    price_total             = models.DecimalField('Общая стоимость (руб.)', max_digits=30, decimal_places=2, blank=True, null=True, help_text='Считается автоматически из Площади помещения * Цена за м2')
    rooms_qty               = models.CharField('Количество комнат в помещении', max_length=100, choices=ROOMS_QTY, blank=True, null=True)
    site_area               = models.DecimalField('Площадь помещения', max_digits=10, decimal_places=2, blank=True, null=True)
    living_area             = models.DecimalField('Жилая площадь', max_digits=10, decimal_places=2, blank=True, null=True)
    kitchen_area            = models.DecimalField('Площадь кухни', max_digits=10, decimal_places=2, blank=True, null=True)
    ceiling_height          = models.DecimalField('Высота потолка (м)', max_digits=10, decimal_places=2, blank=True, null=True, help_text='Пример: 2.30 = 2 метра 30 см')

    two_levels              = models.BooleanField('Двухуровневая квартира', default=False, help_text='Квартира с полноценным 2-м этажом')
    entresol                = models.BooleanField('Антресоль', default=False, help_text='Наличие в квартире этажа-антресоли')
    wardrobe                = models.BooleanField('Гардеробная', default=False, help_text='Помещение для гардеробной или кладовой')

    finish_type             = models.CharField('Отделка', max_length=100, choices=FINISHING_TYPES, blank=True, null=True)
    window_view             = models.ManyToManyField(ObjectSiteWindowsView, verbose_name='Вид из окон', blank=True)

    image_planning          = models.ImageField('Планировка', upload_to=image_upload_path, blank=True, null=True)
    image_planning3d        = models.ImageField('Планировка 3D', upload_to=image_upload_path, blank=True, null=True)
    image_floor             = models.ImageField('Квартира на этаже', upload_to=image_upload_path, blank=True, null=True, help_text='Планировка квартиры на этаже')
    image_section           = models.ImageField('Этаж в секции', upload_to=image_upload_path, blank=True, null=True, help_text='Выделенный этаж в секции объекта')
    image_section_in_object = models.ImageField('Секция в доме', upload_to=image_upload_path, blank=True, null=True, help_text='Выделенная секция в доме')
    image_genplan           = models.ImageField('Дом на генплане', upload_to=image_upload_path, blank=True, null=True, help_text='Выделенный дом на генплане')

    updated                 = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    # Thumbnails for admin
    def image_planning_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_planning.url))
    image_planning_thumb.short_description = 'Планировка (thumbnail)'

    def image_planning3d_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_planning3d.url))
    image_planning3d_thumb.short_description = 'Планировка 3D (thumbnail)'

    def image_floor_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_floor.url))
    image_floor_thumb.short_description = 'Квартира на этаже (thumbnail)'

    def image_section_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_section.url))
    image_section_thumb.short_description = 'Этаж в секции (thumbnail)'

    def image_section_in_object_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_section_in_object.url))
    image_section_in_object_thumb.short_description = 'Секция в доме (thumbnail)'

    def image_genplan_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_genplan.url))
    image_genplan_thumb.short_description = 'Дом на генплане (thumbnail)'
    # END Thumbnails for admin

    def __str__(self):
        return self.crm_id

    def get_absolute_url(self):
        return reverse('object:site-detail', kwargs={"pk": self.id})

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения (квартиры, апартаменты, коммерческие)'


@receiver(pre_save, sender=ObjectSite)
def calculate_total_price(sender, instance, **kwargs):
    if instance.site_area is not None and instance.price_per_square is not None:
        instance.price_total = instance.site_area * instance.price_per_square


@receiver(post_save, sender=ObjectSite)
def image_optimization(sender, instance, created, **kwargs):
    # TODO: Refactor this!!!
    if instance.image_planning:
        image = ImageOptimizer(instance.image_planning.path)
        image.optimizeAndSaveImg()
    if instance.image_planning3d:
        image = ImageOptimizer(instance.image_planning3d.path)
        image.optimizeAndSaveImg()
    if instance.image_floor:
        image = ImageOptimizer(instance.image_floor.path)
        image.optimizeAndSaveImg()
    if instance.image_section:
        image = ImageOptimizer(instance.image_section.path)
        image.optimizeAndSaveImg()
    if instance.image_section_in_object:
        image = ImageOptimizer(instance.image_section_in_object.path)
        image.optimizeAndSaveImg()
    if instance.image_genplan:
        image = ImageOptimizer(instance.image_genplan.path)
        image.optimizeAndSaveImg()


@receiver(post_delete, sender=ObjectSite)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete empty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

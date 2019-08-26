from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.classes.clean_media import CleanMedia
from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object_section import ObjectSection


def image_upload_path(instance, filename):
    object_crm_id = instance.object_section.object.crm_id
    section_id = instance.object_section.number

    filename = FileProcessing(filename)
    filename = filename.newFileNameGenerated()
    return 'objects/{object_crm_id}/section_{section_id}/parking/{filename}'.format(object_crm_id=object_crm_id, section_id=section_id, filename=filename)


class ObjectParking(models.Model):
    object_section   = models.ForeignKey(ObjectSection, verbose_name='Секция Объекта', on_delete=models.CASCADE)
    crm_id           = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    site_number      = models.CharField('Номер помещения', max_length=100, blank=True, null=True)
    floor            = models.IntegerField('Этаж', validators=[MinValueValidator(-5), MaxValueValidator(5)], blank=True, null=True)
    site_area        = models.DecimalField('Площадь помещения', max_digits=6, decimal_places=2, blank=True, null=True)
    price_per_square = models.DecimalField('Цена за м2 (руб.)', max_digits=8, decimal_places=2, blank=True, null=True, help_text='Стоимость одного квадратного метра')
    price_total      = models.DecimalField('Общая стоимость (руб.)', max_digits=11, decimal_places=2, blank=True, null=True, help_text='Считается автоматически из Площади помещения * Цена за м2')
    image_planning         = models.ImageField('Планировка', upload_to=image_upload_path, blank=True, null=True)
    image_planning_parking = models.ImageField('Место на плане паркинга', upload_to=image_upload_path, blank=True, null=True)

    # Thumbnails for admin
    def image_planning_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_planning.url))
    image_planning_thumb.short_description = 'Планировка (thumbnail)'

    def image_planning_parking_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image_planning_parking.url))
    image_planning_parking_thumb.short_description = 'Место на плане паркинга  (thumbnail)'
    # Thumbnails for admin

    def __str__(self):
        return self.crm_id

    class Meta:
        verbose_name = 'Парковочное место'
        verbose_name_plural = 'Парковочные места'


@receiver(pre_save, sender=ObjectParking)
def calculate_total_price(sender, instance, **kwargs):
    if instance.site_area is not None and instance.price_per_square is not None:
        instance.price_total = instance.site_area * instance.price_per_square


@receiver(post_save, sender=ObjectParking)
def image_optimization(sender, instance, created, **kwargs):
    if instance.image_planning:
        image = ImageOptimizer(instance.image_planning.path)
        image.optimizeAndSaveImg()
    if instance.image_planning_parking:
        image = ImageOptimizer(instance.image_planning_parking.path)
        image.optimizeAndSaveImg()


@receiver(post_delete, sender=ObjectParking)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete empty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

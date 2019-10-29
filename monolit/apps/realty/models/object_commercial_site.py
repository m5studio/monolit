from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from apps.realty.models.object_commercial import ObjectCommercial
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection


class ObjectCommercialSite(models.Model):
    SITE_TYPES = (
        ('office', 'Офис'),
        ('free-use', 'Помещение свободного назначения'),
    )

    active            = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    special_offer     = models.BooleanField('Спецпредложение', default=False)

    object_commercial = models.ForeignKey(ObjectCommercial, verbose_name='Коммерческий Объект', on_delete=models.CASCADE)
    site_type         = models.CharField('Тип помещения', max_length=100, default='', choices=SITE_TYPES)

    object_block      = models.ForeignKey(ObjectBlock, verbose_name='Блок Объекта', on_delete=models.SET_NULL, blank=True, null=True)
    object_section    = models.ForeignKey(ObjectSection, verbose_name='Секция Объекта', on_delete=models.SET_NULL, blank=True, null=True)

    crm_id            = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    floor             = models.IntegerField('Этаж', validators=[MinValueValidator(-5), MaxValueValidator(100)], blank=True, null=True)
    site_number       = models.CharField('Номер помещения', max_length=100, blank=True, null=True)

    price_per_square  = models.DecimalField('Цена за м2 (руб.)', max_digits=8, decimal_places=2, blank=True, null=True, help_text='Стоимость одного квадратного метра')
    price_total       = models.DecimalField('Общая стоимость (руб.)', max_digits=11, decimal_places=2, blank=True, null=True, help_text='Считается автоматически из Площади помещения * Цена за м2')

    updated           = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.crm_id

    class Meta:
        verbose_name = 'Коммерческое помещение'
        verbose_name_plural = '2.1 Коммерческие Помещения (Офисы, Cвободного назначения)'


@receiver(pre_save, sender=ObjectCommercialSite)
def calculate_total_price(sender, instance, **kwargs):
    if instance.site_area is not None and instance.price_per_square is not None:
        instance.price_total = instance.site_area * instance.price_per_square

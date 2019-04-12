from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.realty.models.object import Object


class ObjectSite(models.Model):
    SITE_TYPES = (
        ('flat', 'Квартира'),
        ('apartments', 'Апартаменты'),
        ('commercial', 'Коммерческое'),
    )

    ROOMS_QTY = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    status           = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    special_offer    = models.BooleanField('Спецпредложение', default=False)
    object           = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE, blank=True, null=True)
    ste_type         = models.CharField('Тип помещения', max_length=100, choices=SITE_TYPES, blank=True, null=True)
    name             = models.CharField('Название помещения', max_length=255)
    crm_id           = models.CharField('CRM ID', max_length=100, blank=True, null=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    floor            = models.IntegerField('Этаж', validators=[MinValueValidator(-5), MaxValueValidator(100)], blank=True, null=True)
    site_number      = models.CharField('Номер квартиры или помещения', max_length=100, blank=True, null=True)
    price_per_square = models.DecimalField('Цена за м2 (руб.)', max_digits=20, decimal_places=2, blank=True, null=True, help_text='Стоимость одного квадратного метра')
    price_total      = models.DecimalField('Общая стоимость (руб.)', max_digits=30, decimal_places=2, blank=True, null=True)
    rooms_qty        = models.CharField('Количество комнат в помещении', max_length=100, choices=ROOMS_QTY, blank=True, null=True)
    site_area        = models.DecimalField('Площадь помещения', max_digits=10, decimal_places=2, blank=True, null=True)
    living_area      = models.DecimalField('Жилая площадь', max_digits=10, decimal_places=2, blank=True, null=True)
    kitchen_area     = models.DecimalField('Площадь кухни', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.price_total = self.site_area * self.price_per_square
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения (квартиры, апартаменты, коммерческие)'

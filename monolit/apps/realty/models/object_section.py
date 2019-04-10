from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.realty.models.object import Object
from apps.realty.models.object_block import ObjectBlock


class ObjectSection(models.Model):
    object       = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    object_block = models.ForeignKey(ObjectBlock, verbose_name='Блок Объекта', on_delete=models.CASCADE, default=0, blank=True, null=True)
    name         = models.CharField('Номер секции или её название', max_length=255)
    year_finish  = models.PositiveIntegerField('Год сдачи', default='', blank=True, null=True, validators=[MinValueValidator(2019), MaxValueValidator(2100)], help_text='Допустимые значения от 2019 до 2100')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция Объекта'
        verbose_name_plural = 'Объекты (Секции)'

import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.realty.models.object import Object
from apps.realty.models.object_block import ObjectBlock


class ObjectSection(models.Model):
    object                = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE)
    object_block          = models.ForeignKey(ObjectBlock, verbose_name='Блок Объекта', on_delete=models.CASCADE, default=0, blank=True, null=True)
    name                  = models.CharField('Номер секции или её название', max_length=255)
    genplan_svg           = models.TextField('SVG координары выделения секции на Генплане',
                                             blank=True, null=True,
                                             help_text='Выеделение с помощью SVG координат секции на Генплане')
    year_of_construction  = models.PositiveIntegerField('Год сдачи',
                                                        default=datetime.date.today().year,
                                                        blank=True, null=True,
                                                        validators=[
                                                            MinValueValidator(2019),
                                                            MaxValueValidator(2100)
                                                        ],
                                                        help_text='Допустимые значения от 2019 до 2100')
    floor_start           = models.IntegerField('Этаж Первый',
                                                blank=True, null=True,
                                                validators=[
                                                    MinValueValidator(-5), MaxValueValidator(0)
                                                ],
                                                help_text='мин. этаж: -5')
    floor_end             = models.IntegerField('Этаж Последний',
                                                blank=True, null=True,
                                                validators=[
                                                    MinValueValidator(0), MaxValueValidator(100)
                                                ],
                                                help_text='макс. этаж: 100')

    def __str__(self):
        return '{} {}'.format(self.object.name, self.name)

    class Meta:
        verbose_name = 'Секция Объекта'
        verbose_name_plural = 'Объекты (Секции)'

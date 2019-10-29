from django.db import models

from ckeditor.fields import RichTextField

from apps.realty.models.object_types import ObjectTypes
from apps.realty.models.object_building_types import ObjectBuildingTypes
from apps.realty.models.object_cities import ObjectCities


class ObjectCommercial(models.Model):
    active        = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    completed     = models.BooleanField('Строительство завершено', default=False)
    all_sold      = models.BooleanField('Все помещения проданы', default=False, help_text='Все квартиры и помещения проданы')

    order         = models.PositiveIntegerField('Порядок', default=0, blank=True, null=True, help_text='Чем выше число, тем ниже объект в списке')
    crm_id        = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    name          = models.CharField('Название объекта', unique=True, max_length=255, db_index=True)
    slug          = models.SlugField('URL адрес', max_length=100, unique=True, help_text='e.g.: status-house (max 100 chars), получим https://monolit.site/commercial/status-house/')

    object_type   = models.ForeignKey(ObjectTypes, verbose_name='Тип Объекта', on_delete=models.SET_NULL, blank=True, null=True)
    building_type = models.ForeignKey(ObjectBuildingTypes, verbose_name='Тип Здания', on_delete=models.SET_NULL, blank=True, null=True)
    description   = RichTextField('Описание', blank=True, null=True)

    city          = models.ForeignKey(ObjectCities, verbose_name='Город', on_delete=models.SET_NULL, blank=True, null=True)
    address       = models.CharField('Адрес', max_length=255, blank=True, null=True, help_text='Город, улица, номер дома (для завершенных/построенных объектов)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коммерческий Объект'
        verbose_name_plural = '2. Коммерческие Объекты'

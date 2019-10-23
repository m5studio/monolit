from django.db import models


class ObjectTypes(models.Model):
    name              = models.CharField('Название Типа объекта', unique=True, max_length=255)
    name_declension   = models.CharField('Склонение', max_length=255, blank=True, null=True, help_text='Пример: "Жилой квартал" указать "Жилом квартале", "Курортный комплекс" указать "Курортном комплексе"')
    name_abbreviation = models.CharField('Сокращение', max_length=255, blank=True, null=True, help_text='Пример: "Жилой квартал" указать "ЖК" или иные сокращения: ТРЦ, БЦ, КК')
    slug         = models.CharField('Название Типа объекта (eng)', max_length=100, unique=True, blank=True, null=True, help_text='e.g.: если название "Жилой квартал", то здесь заполняется как "living-quarter"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип Объекта'
        verbose_name_plural = 'Типы Объектов'

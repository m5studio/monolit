from django.db import models


class ObjectTypes(models.Model):
    name = models.CharField('Тип объекта', unique=True, max_length=255)
    slug = models.CharField('Тип объекта (eng)', max_length=100, unique=True, blank=True, null=True, help_text='e.g.: если название "Жилой квартал", то здесь заполняется как "living-quarter"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип Объекта'
        verbose_name_plural = 'Типы Объектов'

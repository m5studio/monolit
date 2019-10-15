from django.db import models


class ObjectTypes(models.Model):
    name = models.CharField('Тип объекта', unique=True, max_length=255)
    # slug = models.SlugField('Slug', max_length=100, unique=True, help_text='e.g.: status-house (max 100 chars), получим https://monolit.site/objects/status-house/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип Объекта'
        verbose_name_plural = 'Типы Объектов'

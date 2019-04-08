from django.db import models

from ckeditor.fields import RichTextField

from apps.realty.models.object import Object


class ObjectInfoTab(models.Model):
    object       = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    name         = models.CharField('Название Вкладки', max_length=100)
    description  = RichTextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таб [Информация об объекте]'
        verbose_name_plural = 'Табы [Информация об объекте]'

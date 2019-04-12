from django.db import models
from apps.realty.models.object import Object


class ObjectFile(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    title  = models.CharField('Название документа', max_length=255, blank=True, null=True)
    file   = models.FileField('Файл', upload_to='uploads/objects/files/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фаил Объекта'
        verbose_name_plural = 'Файлы Объектов [Информационный буклет, Генплан объекта недвижимости, Коммерческое предложение]'

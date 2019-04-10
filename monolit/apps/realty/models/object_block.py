from django.db import models
from apps.realty.models.object import Object


class ObjectBlock(models.Model):
    # object = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    name  = models.CharField('Номер блока или его название', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блок Объекта'
        verbose_name_plural = 'Объект Блоки'

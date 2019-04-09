import datetime

from django.db import models
from apps.realty.models.object import Object


class Document(models.Model):
    object  = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    title   = models.CharField('Название документа', max_length=255, blank=True, null=True)
    author  = models.CharField('Автор', max_length=255, blank=True, null=True)
    date    = models.DateField(verbose_name='Дата', default=datetime.date.today)
    file    = models.FileField('Файл', upload_to='uploads/objects/docs/', blank=True, null=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

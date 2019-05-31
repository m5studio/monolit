import datetime
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

from apps.realty.models.object import Object
# from ..realty.models.object import Object


class NewsCategory(models.Model):
    name = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title    = models.CharField('Заголовок новости', max_length=255)
    object   = models.ManyToManyField(Object, verbose_name='Объект(ы)',
                                      blank=True,
                                      help_text='Относится ли данная новость к Объекту(ам)? Если нет, то оставьтепустым')
    category = models.ManyToManyField(NewsCategory, blank=True, verbose_name='Категории новости')
    date     = models.DateField(verbose_name='Дата', default=datetime.date.today)
    body     = RichTextField('Текст новости', blank=True, null=True)
    created  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

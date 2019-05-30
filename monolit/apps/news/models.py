from django.db import models
from django.urls import reverse


class NewsCategory(models.Model):
    name = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ManyToManyField(NewsCategory, verbose_name='Категория новости')
    title    = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.name

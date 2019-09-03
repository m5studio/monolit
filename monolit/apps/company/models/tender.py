from django.utils import timezone
from django.db import models

from ckeditor.fields import RichTextField

from apps.core.classes.clean_media import CleanMedia
from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.image_optimizer import ImageOptimizer


"""
# TODO: 
1. Model TenderFiles
    name
    file

2. TenderFiles Inline to Tender

3. Tender + TenderFiles to API

4. JS combine all files in one .zip archive
"""


class Tender(models.Model):
    CATEGORIES = (
        ('construction', 'Строительство'),
        ('materials', 'Материалы'),
        ('equipment', 'Оборудование'),
        ('projecting', 'Проектирование'),
        ('other', 'Другое'),
    )

    active       = models.BooleanField('Активный', default=True, help_text='Является ли данный Тендер активным?')
    title        = models.CharField('Название тендера', max_length=255)
    category     = models.CharField('Категория тендера', max_length=100, choices=CATEGORIES)
    duties       = RichTextField('Обязанности', blank=True, null=True)
    requirements = RichTextField('Требования', blank=True, null=True)
    contacts     = RichTextField('Контакты', blank=True, null=True)
    date_start   = models.DateTimeField('Срок проведения (начало)', default=timezone.now)
    date_end     = models.DateTimeField('Срок проведения (конец)', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'

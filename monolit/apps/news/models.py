import datetime

from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from apps.core.classes.clean_media import CleanMedia
from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object import Object
# from ..realty.models.object import Object


class NewsCategory(models.Model):
    name = models.CharField('Имя категории', max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title    = models.CharField('Заголовок новости', max_length=255)
    object   = models.ManyToManyField(Object, verbose_name='Объект(ы)',
                                      blank=True,
                                      help_text='Относится ли данная новость к Объекту(ам) недвижимости? Если нет, то оставьте пустым')
    category = models.ManyToManyField(NewsCategory, blank=True, verbose_name='Категории новости')
    date     = models.DateField(verbose_name='Дата', default=datetime.date.today)
    body     = RichTextField('Текст новости', blank=True, null=True)
    created  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


def image_upload_path(instance, filename):
    news_id = instance.news.id
    filename = FileProcessing(filename)
    filename = filename.newFileNameGenerated()
    return 'news/{news_id}/{filename}'.format(news_id=news_id, filename=filename)

class NewsImage(models.Model):
    news  = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', blank=True, upload_to=image_upload_path)

    # Thumbnails for admin
    def image_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.image.url))
    image_thumb.short_description = 'Изображение (thumbnail)'
    # END Thumbnails for admin

    def __str__(self):
        return 'image {0} to [{1}]'.format(self.id, self.news) 

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(post_save, sender=NewsImage)
def image_optimization(sender, instance, created, **kwargs):
    if instance.image:
        image = ImageOptimizer(instance.image.path)
        image.optimizeAndSaveImg()


@receiver(post_delete, sender=NewsImage)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete imagekit chache file
    cleanMedia.cleanImagekitCacheImage(instance.image_thumbnail_admin)
    # Delete empty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

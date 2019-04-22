from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

from apps.settings.classes.clean_media import CleanMedia
from apps.settings.classes.file_processing import FileProcessing
from apps.settings.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object import Object


class Gallery(models.Model):
    object  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE, blank=True, null=True)
    title   = models.CharField('Заголовок галереи', max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        print('[DELETE METHOD Gallery]')
        super(Gallery, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Галерея Объекта'
        verbose_name_plural = 'Объекты (Фото Галереи этапов строительства)'


def upload_path(instance, filename):
    gallery_name = instance.gallery.id

    filename = FileProcessing(filename)
    # filename = filename.newFileNameTranslitSlugify()
    filename = filename.newFileNameGenerated()
    return 'realty/galleries/{0}/{1}'.format(gallery_name, filename)

class Image(models.Model):
    gallery               = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.CASCADE, blank=True, null=True)
    alt                   = models.CharField(max_length=100, blank=True, null=True, help_text='alt изображения')
    image                 = models.ImageField('Изображение', upload_to=upload_path)
    image_thumbnail_admin = ImageSpecField(source='image',
                                           # processors=[ResizeToFill(256, 256)],
                                           processors=[ResizeToFit(256, 256)],
                                           options={'quality': 70})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(pre_save, sender=Gallery)
def change_gallery_title(sender, instance, **kwargs):
    # titling Gallery title
    instance.title = instance.title.title()


@receiver(post_save, sender=Image)
def image_optimization(sender, instance, created, **kwargs):
    if instance.image:
        image = ImageOptimizer(instance.image.path)
        image.optimizeAndSaveImg()


@receiver(post_delete, sender=Image)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()

    # Delete imagekit chache file
    cleanMedia.cleanImagekitCacheImage(instance.image_thumbnail_admin)

    # Delete emty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

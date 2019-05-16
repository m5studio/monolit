from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

from apps.settings.classes.clean_media import CleanMedia
from apps.settings.classes.file_processing import FileProcessing
from apps.settings.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object import Object


class ObjectGallery(models.Model):
    object  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE)
    name   = models.CharField('Заголовок галереи', max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея Объекта'
        verbose_name_plural = 'Объекты (Фото Галереи этапов строительства)'


def image_upload_path(instance, filename):
    object_crm_id = instance.gallery.object.crm_id
    gallery_name = instance.gallery.id

    filename = FileProcessing(filename)
    # filename = filename.newFileNameTranslitSlugify()
    filename = filename.newFileNameGenerated()
    return 'objects/{object_crm_id}/galleries/{gallery_name}/{filename}'.format(object_crm_id=object_crm_id, gallery_name=gallery_name, filename=filename)

class ObjectGalleryImage(models.Model):
    gallery               = models.ForeignKey(ObjectGallery, verbose_name='Галерея', on_delete=models.CASCADE)
    alt                   = models.CharField(max_length=100, blank=True, null=True, help_text='alt изображения')
    image                 = models.ImageField('Изображение', upload_to=image_upload_path)
    image_thumbnail_admin = ImageSpecField(source='image',
                                           # processors=[ResizeToFill(256, 256)],
                                           processors=[ResizeToFit(256, 256)],
                                           options={'quality': 70})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(pre_save, sender=ObjectGallery)
def change_gallery_title(sender, instance, **kwargs):
    # titling Gallery title
    instance.title = instance.title.title()


@receiver(post_save, sender=ObjectGalleryImage)
def image_optimization(sender, instance, created, **kwargs):
    if instance.image:
        image = ImageOptimizer(instance.image.path)
        image.optimizeAndSaveImg()


@receiver(post_delete, sender=ObjectGalleryImage)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete imagekit chache file
    cleanMedia.cleanImagekitCacheImage(instance.image_thumbnail_admin)
    # Delete emty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

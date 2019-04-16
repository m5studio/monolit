from django.db import models

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

from apps.realty.models.object import Object


class Gallery(models.Model):
    object  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE, blank=True, null=True)
    title   = models.CharField('Заголовок галереи', max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея Объекта'
        verbose_name_plural = 'Объекты (Фото Галереи этапов строительства)'


def upload_path(instance, filename):
    gallery_name = instance.gallery.id
    filename = filename.lower()

    import os, uuid
    from django.utils.text import slugify
    from transliterate import translit

    name, ext = os.path.splitext(filename)
    transliterated_name = translit(name, 'ru', reversed=True)
    trasliterated_and_slugified_name = slugify(transliterated_name)

    generated_filename = uuid.uuid4()

    # filename = '{0}{1}'.format(trasliterated_and_slugified_name, ext)
    filename = '{0}{1}'.format(generated_filename, ext)

    return 'realty/galleries/{0}/{1}'.format(gallery_name, filename)

class Image(models.Model):
    gallery               = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.SET_NULL, blank=True, null=True)
    alt                   = models.CharField(max_length=100, blank=True, null=True, help_text='alt изображения')
    image                 = models.ImageField('Изображение', upload_to=upload_path, blank=True, null=True)
    image_thumbnail_admin = ImageSpecField(source='image',
                                           # processors=[ResizeToFill(256, 256)],
                                           processors=[ResizeToFit(256, 256)],
                                           options={'quality': 70})

    # def __str__(self):
    #     return self.alt

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(pre_save, sender=Gallery)
def change_gallery_title(sender, instance, **kwargs):
    # titling Gallery title
    instance.title = instance.title.title()

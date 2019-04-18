from django.db import models

from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
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

    import os, uuid, shutil
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
    image                 = models.ImageField('Изображение', upload_to=upload_path)
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


# @receiver(pre_delete)
# @receiver(pre_delete, sender=Gallery)
@receiver(post_delete, sender=Image)
def pre_clean_empty_dirs(sender, instance, **kwargs):
    print("!!!!!!!!!!!!!!!!!!!!!!!!! PRE_DELETE SIGNAL")


# @receiver(post_delete)
# @receiver(post_delete, sender=Gallery)
@receiver(post_delete, sender=Image)
def post_clean_empty_dirs(sender, instance, **kwargs):
    import os, itertools
    from django.conf import settings

    print("!!!!!!!!!!!!!!!!!!!!!!!!! POST_DELETE SIGNAL")

    # Delete imagekit chache file
    # print(instance.image_thumbnail_admin)
    path_to_cache_file = os.path.join(settings.MEDIA_ROOT, str(instance.image_thumbnail_admin))
    os.remove(path_to_cache_file)

    # Delete empty dirs
    def getEmptyDirs(directory_to_search) -> list:
        emty_dirs = list()
        # for root, dirs, files in os.walk(directory_to_search, topdown=False):
        for root, dirs, files in os.walk(directory_to_search):
            # Get dirs without files
            if not len(dirs) and not len(files):
                emty_dirs.append(root)
        return emty_dirs

    def deleteDir(dir_to_remove):
        try:
            os.rmdir(dir_to_remove)
            print('[REMOVED] ' + dir_to_remove)
        except OSError as e:
            print(e)
            pass

    def deleteEmtyDirs(directory_to_delete):
        return list(map(deleteDir, getEmptyDirs(directory_to_delete)))

    def deleteEmptyDirsRecusive(directory_to_search, repeat=10):
        # repeat deleting iterations N times
        for _ in itertools.repeat(None, repeat):
            for directory in getEmptyDirs(directory_to_search):
                deleteEmtyDirs(directory_to_search)

    deleteEmptyDirsRecusive(settings.MEDIA_ROOT)

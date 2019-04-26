from django.db import models

from django.db.models.signals import post_delete
from django.dispatch import receiver

from apps.settings.classes.clean_media import CleanMedia
from apps.settings.classes.file_processing import FileProcessing

from apps.realty.models.object import Object


def file_upload_path(instance, filename):
    object_crm_id = instance.object.crm_id
    filename = FileProcessing(filename)
    filename = filename.newFileNameTranslitSlugify()
    return 'objects/{object_crm_id}/files/{filename}'.format(object_crm_id=object_crm_id, filename=filename)

class ObjectFile(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    title  = models.CharField('Название документа', max_length=255, blank=True, null=True)
    file   = models.FileField('Файл', upload_to=file_upload_path, blank=True, null=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Фаил Объекта'
        verbose_name_plural = 'Файлы Объектов [Информационный буклет, Генплан объекта недвижимости, Коммерческое предложение]'


@receiver(post_delete, sender=ObjectFile)
def clean_empty_media_dirs(sender, instance, **kwargs):
    cleanMedia = CleanMedia()
    # Delete emty dirs in /media/
    cleanMedia.deleteEmptyDirsRecusive()

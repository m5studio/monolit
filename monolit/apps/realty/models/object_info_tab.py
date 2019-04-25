from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField

from apps.settings.classes.file_processing import FileProcessing
from apps.settings.classes.image_optimizer import ImageOptimizer

from apps.realty.models.object import Object


def image_upload_path(instance, filename):
    object_crm_id = instance.object.crm_id
    filename = FileProcessing(filename)
    filename = filename.newFileNameGenerated()
    return 'objects/{object_crm_id}/info-tabs/{filename}'.format(object_crm_id=object_crm_id, filename=filename)

class ObjectInfoTab(models.Model):
    object       = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    order        = models.PositiveIntegerField('Порядок', default=0, blank=True, null=True, help_text='Чем выше число, тем ниже объект в списке')
    name         = models.CharField('Название Вкладки', max_length=100)
    icon_name    = models.SlugField('Имя иконки', max_length=100, blank=True, null=True, help_text='e.g.: object-about')
    description  = RichTextField('Описание', blank=True, null=True)
    image        = models.ImageField('Изображение', upload_to=image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name

    def image_display(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" alt="" style="width: 128px; height: auto;" />'.format(self.image.url) )
    image_display.short_description = 'Изображение (preview)'

    class Meta:
        verbose_name = 'Таб [Информация об объекте]'
        verbose_name_plural = 'Табы [Информация об объекте: О комплексе, Архитектура, Благоустройство, Расположение, Коммуникации, Планировки, Кладовые...]'


@receiver(post_save, sender=ObjectInfoTab)
def image_optimization(sender, instance, created, **kwargs):
    if instance.image:
        image = ImageOptimizer(instance.image.path)
        image.optimizeAndSaveImg()

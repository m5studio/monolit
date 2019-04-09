from django.db import models
from ckeditor.fields import RichTextField
from apps.realty.models.object import Object


class ObjectInfoTab(models.Model):
    object       = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    order        = models.PositiveIntegerField('Порядок', default=0, blank=True, null=True, help_text='Чем выше число, тем ниже объект в списке')
    name         = models.CharField('Название Вкладки', max_length=100)
    icon_name    = models.SlugField('Имя иконки', max_length=100, blank=True, null=True, help_text='e.g.: object-about')
    description  = RichTextField('Описание', blank=True, null=True)
    image        = models.ImageField('Изображение', upload_to='images/objects/info_tabs/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таб [Информация об объекте]'
        verbose_name_plural = 'Табы [Информация об объекте: О комплексе, Архитектура, Благоустройство, Расположение, Коммуникации, Планировки, Кладовые...]'

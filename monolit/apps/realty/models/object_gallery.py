from django.db import models
# from apps.realty.models.object import Object


class Gallery(models.Model):
    # object  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.CASCADE)
    title   = models.CharField('Заголовок галереи', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея Объекта'
        verbose_name_plural = 'Объекты (Гелереи изображений)'


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея', on_delete=models.SET_NULL, blank=True, null=True)
    title   = models.CharField(max_length=100, blank=True, null=True, help_text='title изображения')
    alt     = models.CharField(max_length=100, blank=True, null=True, help_text='alt изображения')
    image   = models.ImageField('Изображение', upload_to='gallery/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

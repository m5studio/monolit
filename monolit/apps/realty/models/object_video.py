from django.db import models
from apps.realty.models.object import Object


class ObjectVideo(models.Model):
    object    = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    title     = models.CharField('Заголовок видео', max_length=255, blank=True, null=True)
    video_url = models.URLField('Cсылка на видео в YouTube', blank=True, null=True, help_text='e.g.: https://youtu.be/JbacFR_B-jw')
    created   = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.realty.models.object import Object

from apps.core.classes.video_utils import VideoUtils


class ObjectVideo(models.Model):
    object    = models.ForeignKey(Object, on_delete=models.CASCADE, default=0)
    title     = models.CharField('Заголовок видео', max_length=255, blank=True, null=True)
    video     = models.CharField('ID видео в YouTube', max_length=100, blank=True, null=True, help_text='Укажите ссылку: https://www.youtube.com/watch?v=JbacFR_B-jw, https://youtu.be/JbacFR_B-jw или ID видео в YouTube, например: JbacFR_B-jw')
    # created   = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


@receiver(pre_save, sender=ObjectVideo)
def get_youtube_video_code(sender, instance, **kwargs):
    if instance.video_url:
        print('VIDEO URL:')
        print(instance.video_url)
        instance.video_url = VideoUtils.get_youtube_video_id(instance.video_url)

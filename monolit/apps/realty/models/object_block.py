from django.db import models

# from django.db.models.signals import pre_save, post_save, post_delete
# from django.dispatch import receiver

from apps.realty.models.object import Object
from apps.realty.models.object_commercial import ObjectCommercial


class ObjectBlock(models.Model):
    object            = models.ForeignKey(Object, verbose_name='Жилой Объект', on_delete=models.CASCADE, blank=True, null=True)
    object_commercial = models.ForeignKey(ObjectCommercial, verbose_name='Коммерческий Объект', on_delete=models.CASCADE, blank=True, null=True)
    name              = models.CharField('Название блока', max_length=255, blank=True, null=True)

    # TODO:
    # def __str__(self):
        # if self.object.name and self.object_commercial.name == '':
        #     return f'{self.object.name} | {self.name}'
        # if self.object.name == '' and self.object_commercial.name:
        #     return f'{self.object_commercial.name} | {self.name}'
        # if self.object.name == '' and self.object_commercial.name == '':
        #     return f'{self.name}'

        # return f'{self.name}'

    class Meta:
        verbose_name = 'Блок Объекта'
        verbose_name_plural = 'Объект (Блоки)'


# @receiver(pre_save, sender=ObjectBlock)
# def rename_block_name(sender, instance, **kwargs):
#     instance.name = ''
#     instance.name = f'{instance.object.name} {instance.name}'

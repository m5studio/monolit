from django.db import models
from apps.realty.models.object_site import ObjectSite


class ObjectBathroom(models.Model):
    BATHROOMS = (
        ('0', 'Совмещенный'),
        ('1', 'Раздельный'),
    )

    object_site   = models.ForeignKey(ObjectSite, on_delete=models.CASCADE, blank=True, null=True)
    bathroom_type = models.CharField('Тип санузла', max_length=100, choices=BATHROOMS, blank=True, null=True)
    bathroom_qty  = models.PositiveIntegerField('Количество санузлов', default=1, blank=True, null=True)

    def __str__(self):
        return self.bathroom_type

    class Meta:
        verbose_name = 'Санузел'
        verbose_name_plural = 'Санузлы'

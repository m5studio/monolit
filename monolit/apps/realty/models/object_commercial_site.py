from django.db import models

from ckeditor.fields import RichTextField

from apps.realty.models.object_commercial import ObjectCommercial


class ObjectCommercialSite(models.Model):
    active            = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    special_offer     = models.BooleanField('Спецпредложение', default=False)

    object_commercial = models.ForeignKey(ObjectCommercial, verbose_name='Коммерческий Объект', on_delete=models.CASCADE)
    crm_id            = models.CharField('CRM ID', max_length=100, unique=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')

    updated           = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.crm_id

    class Meta:
        verbose_name = 'Коммерческое помещение'
        verbose_name_plural = '2.1 Коммерческие Помещения (Офисы, Cвободного назначения)'

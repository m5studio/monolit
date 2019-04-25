from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.realty.models.object import Object
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection


class ObjectSiteWindowsView(models.Model):
    name = models.CharField('Вид из окон', max_length=255)

    def __str__(self):
        return self.name


class ObjectSite(models.Model):
    SITE_TYPES = (
        ('flat', 'Квартира'),
        ('apartments', 'Апартаменты'),
        ('commercial', 'Коммерческое'),
    )

    ROOMS_QTY = (
        ('0', 'Студия'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    FINISHING_TYPES = (
        ('0', 'Без отделки'),
        ('1', 'Черновая отделка'),
        ('1', 'Чистовая отделка'),
    )

    # WINDOWS_VIEW = (
    #     ('yard', 'Во двор'),
    #     ('street', 'Улица'),
    #     ('sea', 'Море'),
    #     ('lake', 'Озеро'),
    #     ('mountains', 'Горы'),
    # )

    status                  = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    special_offer           = models.BooleanField('Спецпредложение', default=False)
    site_type               = models.CharField('Тип помещения', max_length=100, choices=SITE_TYPES, blank=True, null=True)

    object                  = models.ForeignKey(Object, verbose_name='Объект', on_delete=models.SET_NULL, blank=True, null=True)
    object_block            = models.ForeignKey(ObjectBlock, verbose_name='Блок Объекта', on_delete=models.SET_NULL, blank=True, null=True)
    object_section          = models.ForeignKey(ObjectSection, verbose_name='Секция Объекта', on_delete=models.SET_NULL, blank=True, null=True)

    crm_id                  = models.CharField('CRM ID', max_length=100, unique=True, blank=True, null=True, help_text='ID объекта в 1C (Заполняется автоматически при выгрузке)')
    floor                   = models.IntegerField('Этаж', validators=[MinValueValidator(-5), MaxValueValidator(100)], blank=True, null=True)
    site_number             = models.CharField('Номер квартиры или помещения', max_length=100, blank=True, null=True)
    price_per_square        = models.DecimalField('Цена за м2 (руб.)', max_digits=20, decimal_places=2, blank=True, null=True, help_text='Стоимость одного квадратного метра')
    price_total             = models.DecimalField('Общая стоимость (руб.)', max_digits=30, decimal_places=2, blank=True, null=True, help_text='Считается автоматически из Площади помещения * Цена за м2')
    rooms_qty               = models.CharField('Количество комнат в помещении', max_length=100, choices=ROOMS_QTY, blank=True, null=True)
    site_area               = models.DecimalField('Площадь помещения', max_digits=10, decimal_places=2, blank=True, null=True)
    living_area             = models.DecimalField('Жилая площадь', max_digits=10, decimal_places=2, blank=True, null=True)
    kitchen_area            = models.DecimalField('Площадь кухни', max_digits=10, decimal_places=2, blank=True, null=True)
    ceiling_height          = models.DecimalField('Высота потолков (м)', max_digits=10, decimal_places=2, blank=True, null=True, help_text='Пример: 2.30 = 2 метра 30 см')

    two_levels              = models.BooleanField('Двухуровневая квартира', default=False, help_text='Квартира с полноценным 2-м этажом')
    entresol                = models.BooleanField('Антресоль', default=False, help_text='Наличие в квартире этажа-антресоли')
    wardrobe                = models.BooleanField('Гардеробная', default=False, help_text='Помещение для гардеробной или кладовой')

    finish_type             = models.CharField('Отделка', max_length=100, choices=FINISHING_TYPES, blank=True, null=True)
    window_view             = models.ManyToManyField(ObjectSiteWindowsView, verbose_name='Вид из окон')

    image_planning          = models.ImageField('Планировка', upload_to='objects/', blank=True, null=True)
    image_planning3d        = models.ImageField('Планировка 3D', upload_to='objects/', blank=True, null=True)
    image_floor             = models.ImageField('Квартира на этаже', upload_to='objects/', blank=True, null=True, help_text='Планировка квартиры на этаже')
    image_section           = models.ImageField('Этаж в секции', upload_to='objects/', blank=True, null=True, help_text='Выделенный этаж в секции объекта')
    image_section_in_object = models.ImageField('Секция в доме', upload_to='objects/', blank=True, null=True, help_text='Выделенная секция в доме')
    image_genplan           = models.ImageField('Дом на генплане', upload_to='objects/', blank=True, null=True, help_text='Выделенный дом на генплане')
    updated                 = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.crm_id

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения (квартиры, апартаменты, коммерческие)'


@receiver(pre_save, sender=ObjectSite)
def calculate_total_price(sender, instance, **kwargs):
    instance.price_total = instance.site_area * instance.price_per_square

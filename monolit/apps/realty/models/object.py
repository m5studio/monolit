from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# from apps.realty.models.city import City


class Object(models.Model):
    CATEGORIES = (
        ('living', 'Жилой'),
        ('commercial', 'Коммерческий'),
    )

    CITIES = (
        ('alushta', 'Алушта'),
        ('evpatoriya', 'Евпатория'),
        ('simferopol', 'Симферополь'),
        ('yalta', 'Ялта'),
    )

    active      = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте')
    completed   = models.BooleanField('Строительство завершено', default=False)
    # order     = models.PositiveIntegerField('Порядок', default=0)
    crm_id      = models.CharField('CRM ID', max_length=100, blank=True, null=True, help_text='ID объекта в 1C')
    name        = models.CharField('Название объекта', max_length=255, db_index=True)
    slug        = models.SlugField('URL адрес', max_length=100, help_text='e.g.: object-url-path (max 100 chars)')
    # city        = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Город')
    city        = models.CharField('Город', max_length=100, choices=CITIES)
    cetegory    = MultiSelectField('Категория объекта',
                                   choices=CATEGORIES,
                                   # default=[CATEGORIES[0][0], CATEGORIES[1][0]],
                                   help_text='Выберите категорию(и) объекта недвижимости')
    description = models.TextField('Описание', blank=True, null=True)

    webcam      = models.URLField('Cсылка на web-камеру', blank=True, null=True, help_text='e.g.: https://rtsp.me/embed/3KASrTkG/')
    panoram     = models.URLField('Cсылка на панораму', blank=True, null=True, help_text='e.g.: https://monolit360.com/files/main/index.html?s=pano1692')

    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('object-detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты (Жилые, Коммерческие)'

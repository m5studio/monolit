from django.db import models

from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from ckeditor.fields import RichTextField

from apps.core.classes.file_processing import FileProcessing
from apps.core.classes.singleton_model import SingletonModel

from apps.realty.models.object import Object


def logo_upload_path(instance, filename):
    filename = FileProcessing(filename)
    filename = filename.newFileNameFromField(instance.name, None, 'logo')
    return 'mortgage/banks/{filename}'.format(filename=filename)

class Bank(models.Model):
    name = models.CharField('Название банка', unique=True, max_length=255)
    logo = models.FileField('Логотип банка (svg, png)', validators=[FileExtensionValidator(['svg', 'png'])], upload_to=logo_upload_path, blank=True, null=True)

    # Thumbnails for admin
    def logo_admin_thumb(self):
        return mark_safe('<img src="{}" alt="" style="width: 256px; height: auto;" />'.format(self.logo.url))
    logo_admin_thumb.short_description = 'Thumbnail'
    # END Thumbnails for admin

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


# class MortgageOffer(models.Model):
class Offer(models.Model):
    bank               = models.ForeignKey(Bank, verbose_name='Банк', on_delete=models.CASCADE)
    title              = models.CharField('Название программы', max_length=255, help_text='Название ипотечного кредита')

    # Первоначальный взнос
    first_payment_from = models.DecimalField('от', max_digits=4, decimal_places=2, blank=True, null=True)
    first_payment_to   = models.DecimalField('до', max_digits=4, decimal_places=2, blank=True, null=True)

    # Срок кредита
    loan_term_from     = models.PositiveIntegerField('от', validators=[MinValueValidator(1), MaxValueValidator(50)], blank=True, null=True)
    loan_term_to       = models.PositiveIntegerField('до', validators=[MinValueValidator(1), MaxValueValidator(50)], blank=True, null=True)

    # Проецентная ставка
    rate_from          = models.DecimalField('от', max_digits=4, decimal_places=2, blank=True, null=True)
    rate_to            = models.DecimalField('до', max_digits=4, decimal_places=2, blank=True, null=True)

    description        = RichTextField('Описание', blank=True, null=True, help_text='Описание и дополнительные условия')
    object             = models.ManyToManyField(Object, verbose_name='Объект(ы)', blank=True, help_text='Выберите Объекты подходящие под данную ипотечную программу')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ипотечная программа'
        verbose_name_plural = 'Ипотечные программы'


class WayToBuy(SingletonModel):
    military = models.ManyToManyField(Object, verbose_name='Военная ипотека', related_name='mortgage_object_military', blank=True, help_text='Выберите Объекты подходящие под военную ипотеку')
    mother   = models.ManyToManyField(Object, verbose_name='Материнский капитал', related_name='mortgage_object_mother', blank=True, help_text='Выберите Объекты подходящие под материнский капитал')

    def __str__(self):
        return 'Способы покупки'

    class Meta:
        verbose_name = 'Способы покупки'
        verbose_name_plural = 'Способы покупки'

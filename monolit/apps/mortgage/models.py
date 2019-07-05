from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from ckeditor.fields import RichTextField

from apps.core.classes.file_processing import FileProcessing


def logo_upload_path(instance, filename):
    filename = FileProcessing(filename)
    filename = filename.newFileNameFromField(instance.name, None, 'logo')
    return 'mortgage/banks/{filename}'.format(filename=filename)

class Bank(models.Model):
    name = models.CharField('Название банка', unique=True, max_length=255)
    logo = models.FileField('Логотип банка .svg', validators=[FileExtensionValidator(['svg'])], upload_to=logo_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


class MortgageOffer(models.Model):
    bank               = models.ForeignKey(Bank, verbose_name='Банк', default=None, on_delete=models.CASCADE)
    title              = models.CharField('Название программы', unique=True, max_length=255, help_text='Название ипотечного кредита')

    # Первоначальный взнос
    first_payment_from = models.DecimalField('от', max_digits=4, decimal_places=2, blank=True, null=True)
    first_payment_to   = models.DecimalField('до', max_digits=4, decimal_places=2, blank=True, null=True)

    # Срок кредита
    loan_term_from     = models.PositiveIntegerField('от', validators=[MinValueValidator(1), MaxValueValidator(50)], blank=True, null=True)
    loan_term_to       = models.PositiveIntegerField('до', validators=[MinValueValidator(1), MaxValueValidator(50)], blank=True, null=True)

    # Проецентная ставка
    interest_rate_from = models.DecimalField('от', max_digits=4, decimal_places=2, blank=True, null=True)
    interest_rate_to   = models.DecimalField('до', max_digits=4, decimal_places=2, blank=True, null=True)

    description        = RichTextField('Описание', blank=True, null=True, help_text='Описание и дополнительные условия')

    class Meta:
        verbose_name = 'Ипотечная программа'
        verbose_name_plural = 'Ипотечные программы'


class MortgagePage(models.Model):
    title = models.CharField('Заголовок', unique=True, max_length=255, help_text='Заголовок страницы по ипотеке пример: Материнский капитал, КорпорАктив, Военная ипотека...')

    class Meta:
        verbose_name = 'Страница (Ипотека)'
        verbose_name_plural = 'Страницы (Ипотека)'

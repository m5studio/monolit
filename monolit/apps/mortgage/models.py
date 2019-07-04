from django.db import models


class Bank(models.Model):
    name = models.CharField('Название банка', unique=True, max_length=255)


class MortgageOffer(models.Model):
    title = models.CharField('Название предложения', unique=True, max_length=255, help_text='Название предложения по ипотеке')


class MortgagePage(models.Model):
    title = models.CharField('Заголовок', unique=True, max_length=255, help_text='Заголовок страницы по ипотеке пример: Материнский капитал, КорпорАктив, Военная ипотека...')

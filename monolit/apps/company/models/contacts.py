from django.db import models


class ContactsGroup(models.Model):
    name       = models.CharField('Название группы контактов', max_length=255)
    address    = models.TextField('Адрес', blank=True, null=True)
    work_hours = models.TextField('График работы', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа контактов'
        verbose_name_plural = 'Контакты'


class ContactsItem(models.Model):
    CONTACTS_TYPES = (
        ('phone', 'Телефон'),
        ('email', 'Email'),
    )

    сontacts_group = models.ForeignKey(ContactsGroup, on_delete=models.CASCADE, default=0)
    сontact_type   = models.CharField('Тип контакта', max_length=100, choices=CONTACTS_TYPES)
    contact        = models.CharField('Контакт', max_length=255, help_text='Заполняется номером телефона или email. Например: +79270004411 или mail@monolit.net')

    def __str__(self):
        return self.сontacts_group.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

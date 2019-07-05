from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
# from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

# Checkboxes for ManyToManyField in Admin
from django.db import models
from django.forms import CheckboxSelectMultiple
# END Checkboxes for ManyToManyField in Admin

from apps.mortgage.models import Bank, MortgageOffer, MortgagePage


@admin.register(Bank)
class BankAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields=('logo_admin_thumb',)
    fieldsets = (
        (None, {
            'fields': ('name',),
        }),
        ('Лого', {
            'fields': ('logo_admin_thumb', 'logo')
        }),
    )


@admin.register(MortgageOffer)
class MortgageOfferAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    list_display = ('title', 'bank')

    description_text = 'Если надо заполнить без ОТ и ДО, то заполняем оба поля одинаковыми значениями'

    # Checkboxes for ManyToManyField in Admin
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    # END Checkboxes for ManyToManyField in Admin

    fieldsets = (
        (None, {
            'fields': ('bank', 'title', 'description'),
        }),
        ('Первоначальный взнос %', {
            'fields': (
                ('first_payment_from', 'first_payment_to'),
            ),
            'description': description_text
        }),
        ('Срок кредита (лет)', {
            'fields': (
                ('loan_term_from', 'loan_term_to'),
            ),
            'description': description_text
        }),
        ('Проецентная ставка %', {
            'fields': (
                ('interest_rate_from', 'interest_rate_to'),
            ),
            'description': description_text
        }),
        ('Объекты участвующие в программе', {
            'fields': ('objects',),
        }),
    )


@admin.register(MortgagePage)
class MortgagePageAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass

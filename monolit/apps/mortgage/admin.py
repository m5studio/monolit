from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
# from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.mortgage.models import Bank, MortgageOffer, MortgagePage


@admin.register(Bank)
class BankAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass


@admin.register(MortgageOffer)
class MortgageOfferAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('bank', 'title', 'description'),
        }),
        ('Первоначальный взнос %', {
            'fields': (
                ('first_payment_from', 'first_payment_to'),
            )
        }),
        ('Срок кредита (лет)', {
            'fields': (
                ('loan_term_from', 'loan_term_to'),
            )
        }),
        ('Проецентная ставка %', {
            'fields': (
                ('interest_rate_from', 'interest_rate_to'),
            )
        }),
    )


@admin.register(MortgagePage)
class MortgagePageAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass

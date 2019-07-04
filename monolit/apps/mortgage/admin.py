from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
# from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.mortgage.models import Bank, MortgageOffer, MortgagePage


@admin.register(Bank)
class BankAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass


@admin.register(MortgageOffer)
class MortgageOfferAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass


@admin.register(MortgagePage)
class MortgagePageAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    pass

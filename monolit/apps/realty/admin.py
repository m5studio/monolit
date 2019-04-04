from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging

from apps.realty.models.object import Object


@admin.register(Object)
class ObjectAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    list_display = ('name', 'active', 'updated')
    search_fields = ['name']
    ordering = ('-updated',)

# admin.site.register(Object, ObjectAdmin)

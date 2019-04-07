from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging

from apps.realty.models.object import Object


@admin.register(Object)
class ObjectAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    list_display = ('name', 'order', 'active', 'updated')
    list_editable = ('order',)
    search_fields = ['name']
    # ordering = ('-updated',)
    ordering = ('order',)
    readonly_fields=('crm_id',)

# admin.site.register(Object, ObjectAdmin)

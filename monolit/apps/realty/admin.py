from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging

from apps.realty.models.object import Object
from apps.realty.models.object_info_tab import ObjectInfoTab


class ObjectInfoTabInline(admin.TabularInline):
    model = ObjectInfoTab
    extra = 0

@admin.register(ObjectInfoTab)
class ObjectInfoTabAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


@admin.register(Object)
class ObjectAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectInfoTabInline,
    ]

    list_display = ('name', 'order', 'active', 'updated')
    list_editable = ('order',)
    search_fields = ['name']
    # ordering = ('-updated',)
    ordering = ('order',)
    readonly_fields=('crm_id',)

# admin.site.register(Object, ObjectAdmin)

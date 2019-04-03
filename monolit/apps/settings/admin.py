from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging
from .models import SiteSettings


class SiteSettingsAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Disable mass actions
    actions = None

    # Remove Delete button
    def has_delete_permission(self, request, obj=None):
        return False

    # Remove "Save and add another" button
    def has_add_permission(self, request):
        base_add_permission = super(SiteSettingsAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = SiteSettings.objects.all().count()
            if count == 0:
                return True
        return False

admin.site.register(SiteSettings, SiteSettingsAdmin)

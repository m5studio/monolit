from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging
from .models import SiteSeoSettings, SiteContactSettings


class SiteSeoSettingsAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Disable mass actions
    actions = None

    # Remove Delete button
    def has_delete_permission(self, request, obj=None):
        return False

    # Remove "Save and add another" button
    def has_add_permission(self, request):
        base_add_permission = super(SiteSeoSettingsAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = SiteSeoSettings.objects.all().count()
            if count == 0:
                return True
        return False


admin.site.register(SiteSeoSettings, SiteSeoSettingsAdmin)


class SiteContactSettingsAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Disable mass actions
    actions = None

    # Remove Delete button
    def has_delete_permission(self, request, obj=None):
        return False

    # Remove "Save and add another" button
    def has_add_permission(self, request):
        base_add_permission = super(SiteContactSettingsAdmin, self).has_add_permission(request)
        if base_add_permission:
            count = SiteContactSettings.objects.all().count()
            if count == 0:
                return True
        return False


admin.site.register(SiteContactSettings, SiteContactSettingsAdmin)

from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging
from apps.settings.classes.singleton_model import SingletonAdminModel
from .models import SiteSettings


# class SiteSettingsAdmin(TurnOffAdminLogging, SingletonAdminModel):
#     pass

# admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(SiteSettings, SingletonAdminModel)

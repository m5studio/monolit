from django.contrib import admin
from apps.settings.classes.singleton_model import SingletonAdminModel
from apps.settings.models import SiteSettings


admin.site.register(SiteSettings, SingletonAdminModel)

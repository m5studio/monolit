# Author: https://steelkiwi.com/blog/practical-application-singleton-design-pattern/
from django.db import models
from django.core.cache import cache

from django.contrib import admin


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SingletonAdminModel(admin.ModelAdmin):

    class Meta:
        abstract = True

    # Disable mass actions
    actions = None

    # Remove Delete button
    def has_delete_permission(self, request, obj=None):
        return False

    # Remove "Save and add another" button
    # def has_add_permission(self, request):
    #     base_add_permission = super(SiteSettingsAdmin, self).has_add_permission(request)
    #     if base_add_permission:
    #         count = SiteSettings.objects.all().count()
    #         if count == 0:
    #             return True
    #     return False

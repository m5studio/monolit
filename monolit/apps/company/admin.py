from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
# from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.company.models.certificate import Certificate


@admin.register(Certificate)
class CertificateAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Фото сертификата', {
           'fields': ('image_thumb', 'image')
        }),
    )

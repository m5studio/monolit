from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
# from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.company.models.certificate import Certificate
from apps.company.models.management import Management
from apps.company.models.responsibility import Responsibility
from apps.company.models.job import JobBlock, JobVacancy
from apps.company.models.history import History
from apps.company.models.structure import Structure
from apps.company.models.partner import Partner


""" [ Certificate ] """
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
""" [ END Certificate ] """


""" [ Management ] """
@admin.register(Management)
class ManagementAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('order',)
        }),
        ('Информация о руководителе', {
            'fields': ('surname', 'name', 'patronymic', 'position',)
        }),
        ('Фото Руководителя', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('position', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END Management ] """


""" [ Responsibility ] """
@admin.register(Responsibility)
class ResponsibilityAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('order', 'title', 'body')
        }),
        ('Изображение', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('title', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END Responsibility ] """


""" [ JobBlock ] """
@admin.register(JobBlock)
class JobBlockAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('order', 'title', 'body')
        }),
        ('Изображение', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('title', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END JobBlock ] """


""" [ JobVacancy ] """
@admin.register(JobVacancy)
class JobVacancyAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('order', 'title',)
        }),
        ('Описание вакансии', {
            'fields': ('experience', 'duties', 'requirements', 'terms', 'salary', 'contacts',)
        }),
    )
    list_display = ('title', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END JobVacancy ] """


""" [ History ] """
@admin.register(History)
class HistoryAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('year', 'body',)
        }),
        ('Изображение', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('year',)
    ordering = ('-year',)
""" [ END History ] """


""" [ Structure ] """
@admin.register(Structure)
class StructureAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('order', 'url', 'body')
        }),
        ('Изображение', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('url', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END Structure ] """


""" [ Partner ] """
@admin.register(Partner)
class PartnerAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    readonly_fields = ('image_thumb',)
    fieldsets = (
        (None, {
            'fields': ('order', 'url',)
        }),
        ('Изображение', {
           'fields': ('image_thumb', 'image')
        }),
    )
    list_display = ('url', 'order',)
    list_editable = ('order',)
    ordering = ('order',)
""" [ END Partner ] """

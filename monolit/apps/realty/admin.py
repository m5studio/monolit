from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging

from apps.realty.models.object import Object
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.document import Document
from apps.realty.models.video import Video
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection


class ObjectSectionInline(admin.TabularInline):
    model = ObjectSection
    extra = 0

@admin.register(ObjectSection)
class ObjectSectionAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()
    # pass


class ObjectBlockInline(admin.TabularInline):
    model = ObjectBlock
    extra = 0

@admin.register(ObjectBlock)
class ObjectBlockAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class ObjectFileInline(admin.TabularInline):
    model = ObjectFile
    extra = 3
    max_num = 3

@admin.register(ObjectFile)
class ObjectFileAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    max_num = 5

@admin.register(Video)
class VideoAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1

@admin.register(Document)
class DocumentAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class ObjectInfoTabInline(admin.TabularInline):
    model = ObjectInfoTab
    extra = 1
    max_num = 8

@admin.register(ObjectInfoTab)
class ObjectInfoTabAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


@admin.register(Object)
class ObjectAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectInfoTabInline,
        ObjectBlockInline,
        ObjectSectionInline,
        VideoInline,
        ObjectFileInline,
        DocumentInline,
    ]

    list_display = ('name', 'order', 'active', 'updated', 'created')
    list_editable = ('order',)
    search_fields = ['name']
    ordering = ('order',)
    readonly_fields=('crm_id',)

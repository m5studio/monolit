from django.contrib import admin
from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging

from apps.realty.models.object import Object
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_document import Document
from apps.realty.models.object_video import Video
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_section import ObjectSection
from apps.realty.models.object_gallery import Gallery, Image
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_site_bathroom import ObjectBathroom


class ObjectBathroomInline(admin.TabularInline):
    model = ObjectBathroom
    extra = 0
    max_num = 5

@admin.register(ObjectBathroom)
class ObjectBalconyAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class ObjectBalconyInline(admin.TabularInline):
    model = ObjectBalcony
    extra = 0
    max_num = 5

@admin.register(ObjectBalcony)
class ObjectBalconyAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


@admin.register(ObjectSite)
class ObjectSiteAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectBathroomInline,
        ObjectBalconyInline,
    ]
    readonly_fields=('crm_id', 'price_total')


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

@admin.register(Image)
class ImageAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    # Hide Model from admin index
    def get_model_perms(self, request):
        return dict()


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0

@admin.register(Gallery)
class GalleryAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('title', 'object', 'updated')
    # search_fields = ['galleries']


class ObjectSectionInline(admin.TabularInline):
    model = ObjectSection
    extra = 0

@admin.register(ObjectSection)
class ObjectSectionAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    list_display = ('name', 'object')


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
        GalleryInline,
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
    # autocomplete_fields = ['galleries']

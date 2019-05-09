from django.contrib import admin

from apps.settings.classes.turn_off_admin_logging import TurnOffAdminLogging
from apps.settings.classes.hide_from_admin_index import HideFromAdminIndex

from imagekit.admin import AdminThumbnail

from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_document import ObjectDocument
from apps.realty.models.object_elevator import ObjectElevator
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_section import ObjectSection
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_site_bathroom import ObjectBathroom
from apps.realty.models.object_site import ObjectSiteWindowsView, ObjectSite
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object import ObjectCategory, Object


""" [ ObjectBathroom ] """
class ObjectBathroomInline(admin.TabularInline):
    model = ObjectBathroom
    extra = 0
    max_num = 5

@admin.register(ObjectBathroom)
class ObjectBathroomAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectBathroom ] """


""" [ ObjectBalcony ] """
class ObjectBalconyInline(admin.TabularInline):
    model = ObjectBalcony
    extra = 0
    max_num = 5

@admin.register(ObjectBalcony)
class ObjectBalconyAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectBalcony ] """


""" [ ObjectSiteWindowsView ] """
@admin.register(ObjectSiteWindowsView)
class ObjectSiteWindowsViewAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['name']
""" [ END ObjectSiteWindowsView ] """


""" [ ObjectSite ] """
@admin.register(ObjectSite)
class ObjectSiteAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectBathroomInline,
        ObjectBalconyInline,
    ]
    list_display = ('crm_id', 'object', 'status', 'updated')
    readonly_fields=('price_total',)
    autocomplete_fields = ['object', 'object_section', 'window_view']
""" [ END ObjectSite ] """


""" [ ObjectGalleryImage ] """
class ObjectGalleryImageInline(admin.TabularInline):
    model = ObjectGalleryImage
    extra = 0

    image_thumbnail_admin = AdminThumbnail(image_field='image_thumbnail_admin')
    fields = ('gallery', 'alt', 'image', 'image_thumbnail_admin')
    readonly_fields = ('image_thumbnail_admin',)

@admin.register(ObjectGalleryImage)
class ObjectGalleryImageAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectGalleryImage ] """


""" [ ObjectGallery ] """
class ObjectGalleryInline(admin.TabularInline):
    model = ObjectGallery
    extra = 0

@admin.register(ObjectGallery)
class ObjectGalleryAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectGalleryImageInline,
    ]
    list_display = ('title', 'object', 'updated')
    search_fields = ['object']
    autocomplete_fields = ['object']
""" [ END ObjectGallery ] """


""" [ ObjectElevator ] """
class ObjectElevatorInline(admin.TabularInline):
    model = ObjectElevator
    extra = 0
    max_num = 5

@admin.register(ObjectElevator)
class ObjectElevatorAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectElevator ] """


""" [ ObjectSection ] """
class ObjectSectionInline(admin.TabularInline):
    model = ObjectSection
    extra = 0

@admin.register(ObjectSection)
class ObjectSectionAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectElevatorInline,
    ]
    list_display = ('name', 'object')
    search_fields = ['object']
    autocomplete_fields = ['object', 'object_block']
""" [ END ObjectSection ] """


""" [ ObjectBlock ] """
class ObjectBlockInline(admin.TabularInline):
    model = ObjectBlock
    extra = 0

@admin.register(ObjectBlock)
class ObjectBlockAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['object_block']
""" [ END ObjectBlock ] """


""" [ ObjectFile ] """
class ObjectFileInline(admin.TabularInline):
    model = ObjectFile
    extra = 3
    max_num = 3

@admin.register(ObjectFile)
class ObjectFileAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectFile ] """


""" [ ObjectVideo ] """
class ObjectVideoInline(admin.TabularInline):
    model = ObjectVideo
    extra = 1
    max_num = 5

@admin.register(ObjectVideo)
class ObjectVideoAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectVideo ] """


""" [ ObjectDocument ] """
class ObjectDocumentInline(admin.TabularInline):
    model = ObjectDocument
    extra = 1

@admin.register(ObjectDocument)
class ObjectDocumentAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectDocument ] """


""" [ ObjectInfoTab ] """
class ObjectInfoTabInline(admin.TabularInline):
    model = ObjectInfoTab
    extra = 1
    max_num = 8

    fields = ('object', 'order', 'name', 'icon_name', 'description', 'image', 'image_preview',)
    readonly_fields = ('image_preview',)

@admin.register(ObjectInfoTab)
class ObjectInfoTabAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectInfoTab ] """


""" [ ObjectCategory ] """
@admin.register(ObjectCategory)
class ObjectCategory(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['name']
""" [ END ObjectCategory ] """


""" [ Object ] """
@admin.register(Object)
class ObjectAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        ObjectInfoTabInline,
        ObjectBlockInline,
        ObjectSectionInline,
        ObjectVideoInline,
        ObjectFileInline,
        ObjectDocumentInline,
    ]

    # fields = ('active', 'completed', 'order', 'crm_id',
    #           ('name', 'slug'),
    #           'category', 'object_type', 'building_type', 'city', 'address', 'location', 'description', 'has_military', 'has_mother', 'webcam', 'panoram')
    readonly_fields = ('genplan_preview',)

    fieldsets = (
        (None, {
            'fields': ('active', 'completed', 'order', 'crm_id', 'name', 'slug', 'category', 'object_type', 'building_type', 'city', 'address', 'location', 'description', 'has_military', 'has_mother', 'webcam', 'panoram')
        }),
        ('Генплан', {
           'fields': ('genplan_preview', 'genplan')
        }),
    )

    list_display = ('name', 'crm_id', 'order', 'active', 'updated')
    list_editable = ('order', 'active')
    search_fields = ['name']
    ordering = ('order',)
    autocomplete_fields = ['category']
""" [ END Object ] """

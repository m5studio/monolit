from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from imagekit.admin import AdminThumbnail

from apps.realty.models.object_block import ObjectBlock
from apps.realty.models.object_document import ObjectDocument, ObjectDocumentAuthor
from apps.realty.models.object_elevator import ObjectElevator
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_section import ObjectSection
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_site_bathroom import ObjectBathroom
from apps.realty.models.object_site import ObjectSiteWindowsView, ObjectSite
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object import Object
# from apps.realty.models.object_types import ObjectTypes
from apps.realty.models.odject_types import ObjectTypes


""" [ ObjectBathroom ] """
class ObjectBathroomInline(admin.TabularInline):
    model = ObjectBathroom
    extra = 0
    max_num = 2

@admin.register(ObjectBathroom)
class ObjectBathroomAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectBathroom ] """


""" [ ObjectBalcony ] """
class ObjectBalconyInline(admin.TabularInline):
    model = ObjectBalcony
    extra = 0
    max_num = 4

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

    readonly_fields=('price_total', 'image_planning_thumb', 'image_planning3d_thumb', 'image_floor_thumb', 'image_section_thumb', 'image_section_in_object_thumb', 'image_genplan_thumb')
    fieldsets = (
        (None, {
            'fields': ('active', 'special_offer', 'object', 'site_type', 'object_block', 'object_section', 'crm_id', 'floor', 'site_number', 'price_per_square', 'price_total', 'rooms_qty', 'site_area', 'living_area', 'kitchen_area', 'ceiling_height', 'two_levels', 'entresol', 'wardrobe', 'finish_type', 'window_view')
        }),
        ('Изображения', {
           'fields': (
                ('image_planning_thumb', 'image_planning'),
                ('image_planning3d_thumb', 'image_planning3d'),
                ('image_floor_thumb', 'image_floor'),
                ('image_section_thumb', 'image_section'),
                ('image_section_in_object_thumb', 'image_section_in_object'),
                ('image_genplan_thumb', 'image_genplan')
            )
        }),
    )
    list_display = ('crm_id', 'object', 'site_type', 'rooms_qty', 'site_area', 'active', 'special_offer', 'updated')
    list_editable = ('active', 'special_offer')
    list_filter = ('object', 'rooms_qty')

    autocomplete_fields = ['object', 'object_block', 'object_section', 'window_view']
""" [ END ObjectSite ] """


""" [ ObjectGalleryImage ] """
class ObjectGalleryImageInline(admin.TabularInline):
    model = ObjectGalleryImage
    extra = 0

    image_thumb = AdminThumbnail(image_field='image_thumb')
    fields = ('gallery', 'image', 'image_thumb')
    readonly_fields = ('image_thumb',)

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
    list_display = ('name', 'order', 'object', 'updated')
    list_editable = ('order',)
    search_fields = ['object']
    autocomplete_fields = ['object']

    # def get_fields(self, request, obj=None):
    #     if obj:
    #         return ['name', 'order', 'object']
    #     return ['name', 'object']
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

    search_fields = ['object_block']
    autocomplete_fields = ['object_block']

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


""" [ ObjectDocumentAuthor ] """
@admin.register(ObjectDocumentAuthor)
class ObjectDocumentAuthorAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['author']
""" [ END ObjectDocumentAuthor ] """


""" [ ObjectDocument ] """
class ObjectDocumentInline(admin.TabularInline):
    model = ObjectDocument
    extra = 1
    autocomplete_fields = ['author']

@admin.register(ObjectDocument)
class ObjectDocumentAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectDocument ] """


""" [ ObjectTypesAdmin ] """
@admin.register(ObjectTypes)
class ObjectTypesAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['name']
""" [ END ObjectTypesAdmin ] """


""" [ ObjectInfoTab ] """
class ObjectInfoTabInline(admin.TabularInline):
    model = ObjectInfoTab
    extra = 1
    max_num = 8

    readonly_fields = ('image_thumb',)
    fields = ('object', 'icon_name', 'description', 'image', 'image_thumb',)

@admin.register(ObjectInfoTab)
class ObjectInfoTabAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END ObjectInfoTab ] """


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

    readonly_fields = ('genplan_thumb', 'main_image_thumb_admin')
    fieldsets = (
        ('Опции', {
            'fields': ('active', 'completed', 'all_sold', 'partnership')
        }),
        (None, {
            'fields': ('order', 'crm_id', 'name', 'slug', 'object_type', 'building_type', 'description', 'webcam', 'panoram'),
            # 'description': 'Some description if needed'
        }),
        ('Главное изображение', {
            'fields': ('main_image_thumb_admin', 'main_image')
        }),
        ('Генплан', {
            'fields': ('genplan_thumb', 'genplan', 'genplan_svg')
        }),
        ('Адрес', {
            'fields': ('address',)
        }),
    )
    list_display = ('name', 'crm_id', 'order', 'active', 'all_sold', 'partnership', 'updated')
    list_editable = ('order', 'active')
    search_fields = ['name']
    ordering = ('order',)
    autocomplete_fields = ['object_type']
""" [ END Object ] """

from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.news.models import NewsCategory, News, NewsImage


@admin.register(NewsCategory)
class NewsCategoryAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['name']


""" [ NewsImage ] """
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0
    max_num = 50

    readonly_fields = ('image_thumb',)

@admin.register(NewsImage)
class NewsImageAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    pass
""" [ END NewsImage ] """


@admin.register(News)
class NewsAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    inlines = [
        NewsImageInline,
    ]

    readonly_fields = ('main_image_admin_thumb',)
    fieldsets = (
        (None, {
            'fields': ('title', 'object', 'category', 'date', 'body')
        }),
        ('Главное изображение', {
           'fields': ('main_image_admin_thumb', 'main_image')
        }),
    )
    list_display = ('title', 'updated')
    autocomplete_fields = ['object', 'category']

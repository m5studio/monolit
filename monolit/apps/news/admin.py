from django.contrib import admin

from apps.core.classes.turn_off_admin_logging import TurnOffAdminLogging
from apps.core.classes.hide_from_admin_index import HideFromAdminIndex

from apps.news.models import NewsCategory, News


@admin.register(NewsCategory)
class NewsCategoryAdmin(TurnOffAdminLogging, HideFromAdminIndex, admin.ModelAdmin):
    search_fields = ['name']


@admin.register(News)
class NewsAdmin(TurnOffAdminLogging, admin.ModelAdmin):
    autocomplete_fields = ['object', 'category']

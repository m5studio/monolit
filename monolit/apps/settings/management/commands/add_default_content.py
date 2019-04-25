""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError

from apps.realty.models.object import ObjectCategory
from apps.realty.models.object_site import ObjectSiteWindowsView

from apps.settings.models import SiteSettings


class Command(BaseCommand):
    help = 'Create Default content'

    # Create default object categories and window views
    def _create_categories_and_window_views(self, object_name, values):
        for val in values:
            try:
                object_name.objects.get(name=val)
                self.stdout.write(self.style.ERROR('OBJECT: {0} | ALREADY EXIST: {1}'.format(object_name, val)))
            except object_name.DoesNotExist:
                object_name.objects.create(name=val)
                self.stdout.write(self.style.SUCCESS('OBJECT: {0} | CREATED: {1}'.format(object_name, val)))


    # Let's fire it up
    def handle(self, *args, **options):
        obj_categories = ['Жилой', 'Коммерческий']
        self._create_categories_and_window_views(ObjectCategory, obj_categories)

        window_views = ['Во двор', 'Улица', 'Море', 'Озеро', 'Горы']
        self._create_categories_and_window_views(ObjectSiteWindowsView, window_views)

        # self.stdout.write(self.style.SUCCESS('WOW!!! it Works!!!'))
        # self.stdout.write(self.style.ERROR('WOW!!! it won\'t Works!!!'))

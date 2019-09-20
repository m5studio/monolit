""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError

from apps.realty.models.object import ObjectCategory
from apps.realty.models.object_site import ObjectSiteWindowsView
from apps.core.models import SiteSettings
from apps.mortgage.models import WayToBuy


class Command(BaseCommand):
    help = 'Create Default content'

    # Create default object categories and window views
    def _add_content_to_db(self, object_name, values):
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
        self._add_content_to_db(ObjectCategory, obj_categories)

        window_views = ['Во двор', 'Улица', 'Море', 'Озеро', 'Горы']
        self._add_content_to_db(ObjectSiteWindowsView, window_views)

        # Add default content to settings
        # SiteSettings.objects.filter(id=1).update(
        SiteSettings.objects.filter(id=1).update_or_create(
            site_title='Квартиры от застройщика ГК «Монолит» в Крыму',
            site_description='ГК «Монолит» продажа квартир и коммерческих объектов от застройщика в Крыму без посредников',
            site_email='rielt@monolit.net',
            site_phone='+79784447711',
            site_instagram='https://instagram.com/monolit.crimea/',
            site_facebook='https://facebook.com/monolit',
            site_vk='https://vk.com/monolit.crimea',
            site_telegram='https://t.me/monolitstroit',
        )
        self.stdout.write(self.style.SUCCESS('SiteSettings UPDATED'))

        # self.stdout.write(self.style.SUCCESS('WOW!!! it Works!!!'))
        # self.stdout.write(self.style.ERROR('WOW!!! it won\'t Works!!!'))

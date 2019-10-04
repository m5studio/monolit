""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError

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
        # obj_categories = ['Жилой', 'Коммерческий']
        # self._add_content_to_db(ObjectCategory, obj_categories)

        window_views = ['Во двор', 'Улица', 'Море', 'Озеро', 'Горы']
        self._add_content_to_db(ObjectSiteWindowsView, window_views)

        # Add default content to settings
        try:
            site_settings = SiteSettings.objects.get(id=1)
        except SiteSettings.DoesNotExist:
            site_settings = None

        default_content = {
            "site_title": 'Квартиры в Крыму от застройщика ГК Монолит',
            "site_description": 'ГК «Монолит» продажа квартир и коммерческих объектов от застройщика в Крыму без посредников',
            "site_email": 'rielt@monolit.net',
            "site_phone": '+79784447711',
            "site_instagram":'https://instagram.com/monolit.crimea/',
            "site_facebook": 'https://facebook.com/monolit',
            "site_vk": 'https://vk.com/monolit.crimea',
            "site_telegram": 'https://t.me/monolitstroit',
        }

        if site_settings:
            SiteSettings.objects.filter(id=1).update(
                site_title=default_content['site_title'],
                site_description=default_content['site_description'],
                site_email=default_content['site_email'],
                site_phone=default_content['site_phone'],
                site_instagram=default_content['site_instagram'],
                site_facebook=default_content['site_facebook'],
                site_vk=default_content['site_vk'],
                site_telegram=default_content['site_telegram'],
            )
        elif not site_settings:
            SiteSettings.objects.filter(id=1).update_or_create(
                site_title=default_content['site_title'],
                site_description=default_content['site_description'],
                site_email=default_content['site_email'],
                site_phone=default_content['site_phone'],
                site_instagram=default_content['site_instagram'],
                site_facebook=default_content['site_facebook'],
                site_vk=default_content['site_vk'],
                site_telegram=default_content['site_telegram'],
            )

        self.stdout.write(self.style.SUCCESS('SiteSettings UPDATED'))

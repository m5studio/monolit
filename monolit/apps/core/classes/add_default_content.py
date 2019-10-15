from apps.core.models import SiteSettings
from apps.realty.models.object_site import ObjectSiteWindowsView


class AddDefaultContent:
    def add_SiteSettings(self):
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

        try:
            SiteSettings.objects.get(id=1)
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
            print('SiteSettings Updated')
        except SiteSettings.DoesNotExist:
            SiteSettings.objects.filter(id=1).create(
                site_title=default_content['site_title'],
                site_description=default_content['site_description'],
                site_email=default_content['site_email'],
                site_phone=default_content['site_phone'],
                site_instagram=default_content['site_instagram'],
                site_facebook=default_content['site_facebook'],
                site_vk=default_content['site_vk'],
                site_telegram=default_content['site_telegram'],
            )
            print('SiteSettings Created')


    def add_ObjectSiteWindowsView(self):
        window_views = ['Во двор', 'Улица', 'Море', 'Озеро', 'Горы']
        for window_view in window_views:
            try:
                ObjectSiteWindowsView.objects.get(name=window_view)
                print(f'ObjectSiteWindowsView {window_view} already exist and updated')
            except ObjectSiteWindowsView.DoesNotExist:
                ObjectSiteWindowsView.objects.create(name=window_view)
                print(f'ObjectSiteWindowsView {window_view} created')


    def addContent(self):
        self.add_SiteSettings()
        self.add_ObjectSiteWindowsView()

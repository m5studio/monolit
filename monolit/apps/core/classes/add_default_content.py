from apps.core.models import SiteSettings

from apps.realty.models.object_site import ObjectSiteWindowsView
from apps.realty.models.object_types import ObjectTypes
from apps.realty.models.object_building_types import ObjectBuildingTypes


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
                print(f'ObjectSiteWindowsView {window_view} already exist')
            except ObjectSiteWindowsView.DoesNotExist:
                ObjectSiteWindowsView.objects.create(name=window_view)
                print(f'ObjectSiteWindowsView {window_view} created')


    def add_ObjectTypes(self):
        object_types = [
            ('business_center', 'Бизнес центр', 'Бизнес центре', 'БЦ'),
            ('city', 'Город', 'Городе', ''),
            ('living-house', 'Жилой дом', 'Жилом доме', ''),
            ('living-quarter', 'Жилой квартал', 'Жилом квартале', ''),
            ('living-complex', 'Жилой комплекс', 'Жилом комплексе', 'ЖК'),
            ('resort-complex', 'Курортный комплекс', 'Курортном комплексе', ''),
            ('multipurposes-complex', 'Многофункциональный комплекс', 'Многофункциональном комплексе', 'МФК'),
            ('family-quarter', 'Семейный квартал', 'Семейном квартале', ''),
            ('business-and-retail-center', 'Торгово-офисный центр', 'Торгово-офисном центре', ''),
            ('mall', 'Торговый центр', 'Торговом центре', 'ТЦ'),
        ]

        for object_type in object_types:
            name = object_type[1]
            slug = object_type[0]
            name_declension = object_type[2]
            name_abbreviation = object_type[3]

            try:
                ObjectTypes.objects.get(name=name)
                print(f'ObjectTypes {name} already exist')
            except ObjectTypes.DoesNotExist:
                ObjectTypes.objects.create(name=name, name_declension=name_declension, name_abbreviation=name_abbreviation, slug=slug)
                print(f'ObjectTypes {name} created')


    def add_ObjectBuildingTypes(self):
        building_types = [
            ('monolith', 'Монолитный'),
            ('monolith-frame', 'Монолитно-каркасный'),
            ('panel', 'Панельный'),
        ]

        for building_type in building_types:
            name = building_type[1]
            slug = building_type[0]

            try:
                ObjectBuildingTypes.objects.get(name=name)
                print(f'ObjectBuildingTypes {name} already exist')
            except ObjectBuildingTypes.DoesNotExist:
                ObjectBuildingTypes.objects.create(name=name, slug=slug)
                print(f'ObjectBuildingTypes {name} created')


    def addContent(self):
        self.add_SiteSettings()
        self.add_ObjectSiteWindowsView()
        self.add_ObjectTypes()
        self.add_ObjectBuildingTypes()

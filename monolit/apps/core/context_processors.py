import datetime

from apps.core.models import SiteSettings
from apps.realty.models.object import Object


def settings(request):
    return {'settings': SiteSettings.load()}


def monolit_objects(request):
    return {'monolit_objects': Object.objects.filter(active=True, all_sold=False).order_by('order')}


def monolit_company_age(request):
    now = datetime.datetime.now()
    return {'monolit_company_age': now.year - 2005}

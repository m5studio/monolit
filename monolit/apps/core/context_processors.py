# from .models import SiteSettings
from apps.core.models import SiteSettings
from apps.realty.models.object import Object


def settings(request):
    return {'settings': SiteSettings.load()}


def monolit_objects(request):
    return {
            'monolit_objects': Object.objects.filter(active=True, all_sold=False).order_by('order')
        }

from django.db.models import Min, Max

from django.views.generic import TemplateView

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.mortgage.models import Offer
from apps.news.models import News


class HomepageView(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Object.objects.filter(active=True, all_sold=False).order_by('order')
        context['objects_qty'] = Object.objects.filter(active=True, all_sold=False).count()
        context['objects_sold'] = Object.objects.filter(active=True, all_sold=True).order_by('order')
        context['mortgage_offers'] = Offer.objects.order_by('?')[:5]
        context['news_list'] = News.objects.filter(active=True).order_by('-updated')[:5]

        # context['count_object_sites_room_0_site_area_min']   = ObjectSite.objects.filter(active=True, rooms_qty=0).aggregate(Min('site_area'))
        context['count_object_sites_room_0_site_area_min']   = ObjectSite.objects.count_object_sites_room_0_site_area_min()

        context['count_object_sites_room_0_site_area_max']   = ObjectSite.objects.filter(active=True, rooms_qty=0, site_type__in=['flat', 'apartments']).aggregate(Max('site_area'))
        context['count_object_sites_room_0_price_total_min'] = ObjectSite.objects.filter(active=True, rooms_qty=0, site_type__in=['flat', 'apartments']).aggregate(Min('price_total'))

        context['count_object_sites_room_1_site_area_min']   = ObjectSite.objects.filter(active=True, rooms_qty=1, site_type__in=['flat', 'apartments']).aggregate(Min('site_area'))
        context['count_object_sites_room_1_site_area_max']   = ObjectSite.objects.filter(active=True, rooms_qty=1, site_type__in=['flat', 'apartments']).aggregate(Max('site_area'))
        context['count_object_sites_room_1_price_total_min'] = ObjectSite.objects.filter(active=True, rooms_qty=1, site_type__in=['flat', 'apartments']).aggregate(Min('price_total'))

        context['count_object_sites_room_2_site_area_min']   = ObjectSite.objects.filter(active=True, rooms_qty=2, site_type__in=['flat', 'apartments']).aggregate(Min('site_area'))
        context['count_object_sites_room_2_site_area_max']   = ObjectSite.objects.filter(active=True, rooms_qty=2, site_type__in=['flat', 'apartments']).aggregate(Max('site_area'))
        context['count_object_sites_room_2_price_total_min'] = ObjectSite.objects.filter(active=True, rooms_qty=2, site_type__in=['flat', 'apartments']).aggregate(Min('price_total'))

        context['count_object_sites_room_3_site_area_min']   = ObjectSite.objects.filter(active=True, rooms_qty=3, site_type__in=['flat', 'apartments']).aggregate(Min('site_area'))
        context['count_object_sites_room_3_site_area_max']   = ObjectSite.objects.filter(active=True, rooms_qty=3, site_type__in=['flat', 'apartments']).aggregate(Max('site_area'))
        context['count_object_sites_room_3_price_total_min'] = ObjectSite.objects.filter(active=True, rooms_qty=3, site_type__in=['flat', 'apartments']).aggregate(Min('price_total'))

        context['count_object_sites_room_4_site_area_min']   = ObjectSite.objects.filter(active=True, rooms_qty__gte=4, site_type__in=['flat', 'apartments']).aggregate(Min('site_area'))
        context['count_object_sites_room_4_site_area_max']   = ObjectSite.objects.filter(active=True, rooms_qty__gte=4, site_type__in=['flat', 'apartments']).aggregate(Max('site_area'))
        context['count_object_sites_room_4_price_total_min'] = ObjectSite.objects.filter(active=True, rooms_qty__gte=4, site_type__in=['flat', 'apartments']).aggregate(Min('price_total'))

        return context

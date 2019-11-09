from django.views.generic import View, TemplateView
from django.shortcuts import redirect

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.mortgage.models import Offer
from apps.news.models.news import News


class HomepageView(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Object.objects.filter(active=True, all_sold=False).order_by('order')
        context['objects_qty'] = Object.objects.filter(active=True, all_sold=False).count()
        # context['objects_sold'] = Object.objects.filter(active=True, all_sold=True).order_by('order')
        context['mortgage_offers'] = Offer.objects.order_by('?')[:5]
        context['news_list'] = News.objects.filter(active=True).order_by('-updated')[:5]

        context['count_object_sites_room_0_site_area_min']   = ObjectSite.objects.count_object_sites_site_area_min(0)
        context['count_object_sites_room_0_site_area_max']   = ObjectSite.objects.count_object_sites_site_area_max(0)
        context['count_object_sites_room_0_price_total_min'] = ObjectSite.objects.count_object_sites_price_total_min(0)

        context['count_object_sites_room_1_site_area_min']   = ObjectSite.objects.count_object_sites_site_area_min(1)
        context['count_object_sites_room_1_site_area_max']   = ObjectSite.objects.count_object_sites_site_area_max(1)
        context['count_object_sites_room_1_price_total_min'] = ObjectSite.objects.count_object_sites_price_total_min(1)

        context['count_object_sites_room_2_site_area_min']   = ObjectSite.objects.count_object_sites_site_area_min(2)
        context['count_object_sites_room_2_site_area_max']   = ObjectSite.objects.count_object_sites_site_area_max(2)
        context['count_object_sites_room_2_price_total_min'] = ObjectSite.objects.count_object_sites_price_total_min(2)

        context['count_object_sites_room_3_site_area_min']   = ObjectSite.objects.count_object_sites_site_area_min(3)
        context['count_object_sites_room_3_site_area_max']   = ObjectSite.objects.count_object_sites_site_area_max(3)
        context['count_object_sites_room_3_price_total_min'] = ObjectSite.objects.count_object_sites_price_total_min(3)

        context['count_object_sites_room_4_site_area_min']   = ObjectSite.objects.count_object_sites_site_area_min(4, 'gte')
        context['count_object_sites_room_4_site_area_max']   = ObjectSite.objects.count_object_sites_site_area_max(4, 'gte')
        context['count_object_sites_room_4_price_total_min'] = ObjectSite.objects.count_object_sites_price_total_min(4, 'gte')

        return context

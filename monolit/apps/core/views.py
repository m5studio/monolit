# from django.shortcuts import render
from django.views.generic import TemplateView

from apps.realty.models.object import Object
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
        return context

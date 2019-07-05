from django.shortcuts import render
from django.views.generic import TemplateView

from apps.realty.models.object import Object


class HomepageView(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Object.objects.filter(active=True, all_sold=False).order_by('order')
        context['objects_qty'] = Object.objects.filter(active=True, all_sold=False).count()
        context['objects_sold'] = Object.objects.filter(active=True, all_sold=True).order_by('order')
        return context

from django.views.generic import TemplateView

from apps.mortgage.models import MortgageOffer
from apps.realty.models.object import Object


class MortgageView(TemplateView):
    template_name = 'mortgage/mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Ипотека'
        context['mortgage_offers'] = MortgageOffer.objects.all()
        return context


class MortgageCorporactiveView(TemplateView):
    template_name = 'mortgage/corporactive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Корпорактив'
        return context


class MortgageMilitaryView(TemplateView):
    template_name = 'mortgage/military.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Военная ипотека'
        context['objects_military'] = Object.objects.filter(active=True, mortgage_military=True, all_sold=False).order_by('order')
        return context


class MortgageMotherView(TemplateView):
    template_name = 'mortgage/mother.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Материнский капитал'
        return context

from django.views.generic import TemplateView


class MortgageView(TemplateView):
    template_name = 'mortgage/mortgage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Ипотека'
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
        return context


class MortgageMotherView(TemplateView):
    template_name = 'mortgage/mother.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'Материнский капитал'
        return context

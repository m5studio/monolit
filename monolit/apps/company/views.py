from django.views.generic import TemplateView

from apps.company.models.certificate import Certificate


class CompanyView(TemplateView):
    template_name = 'company/company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_tite'] = 'О компании'
        context['certificates'] = Certificate.objects.all()
        return context

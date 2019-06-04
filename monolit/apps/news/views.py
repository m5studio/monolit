from django.views.generic import ListView, DetailView

from apps.news.models import News


class NewsListView(ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = News.objects.all().order_by('-updated')
        return context


class NewsDetailView(DetailView):
    model = News

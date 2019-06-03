from django.views.generic import ListView, DetailView

from apps.news.models import News


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News

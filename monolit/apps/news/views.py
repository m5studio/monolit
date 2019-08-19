from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.news.models import News, NewsImage


class NewsListView(ListView):
    model = News
    queryset = News.objects.filter(active=True).order_by('-updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Новости'
        context['page_meta_description'] = 'Новости Группы Компаний Монолит'

        # context['object_list'] = News.objects.filter(active=True).order_by('-updated')

        # Object list pagination
        paginator = Paginator(context['object_list'], 11)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        # END Object list pagination

        return context


class NewsDetailView(DetailView):
    model = News
    queryset = News.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = News._meta
        context['news_images'] = NewsImage.objects.filter(news=self.get_object().pk)
        context['other_news'] = News.objects.all().exclude(id=self.get_object().pk).order_by('?')[:6]
        return context

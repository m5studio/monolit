# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_file import ObjectFile


class ObjectListView(ListView):
    model = Object

class ObjectDetailView(DetailView):
    model = Object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_info_tabs'] = ObjectInfoTab.objects.filter(object_id=self.get_object().pk).order_by('-order')
        context['object_files'] = ObjectFile.objects.filter(object_id=self.get_object().pk)
        return context


class ObjectSiteListView(ListView):
    model = ObjectSite

class ObjectSiteDetailView(DetailView):
    model = ObjectSite

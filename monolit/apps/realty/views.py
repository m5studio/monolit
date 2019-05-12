# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite


class ObjectListView(ListView):
    model = Object

class ObjectDetailView(DetailView):
    model = Object


class ObjectSiteListView(ListView):
    model = ObjectSite

class ObjectSiteDetailView(DetailView):
    model = ObjectSite

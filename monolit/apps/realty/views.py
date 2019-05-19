# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import (ObjectGallery, ObjectGalleryImage)


class ObjectListView(ListView):
    model = Object
    queryset = Object.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Объекты'
        return context


class ObjectDetailView(DetailView):
    model = Object
    queryset = Object.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = '{object_type} {name}'.format(name=self.get_object().name, object_type=self.get_object().get_object_type_display())
        # context['page_meta_description'] = 'my custom meta'
        context['object_info_tabs'] = ObjectInfoTab.objects.filter(object_id=self.get_object().pk).order_by('-order')
        context['object_files'] = ObjectFile.objects.filter(object_id=self.get_object().pk)

        context['object_galleries'] = ObjectGallery.objects.filter(object=self.get_object().pk).order_by('-order')
        # context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk)
        # context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=self.request.GET.get('gallery_id'))
        # context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=self.request.POST.get('gallery_id'))
        context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=context['object_galleries'].first())

        # Galleries filter
        if self.request.method == "GET" and self.request.GET.get('gallery_id'):
            context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=self.request.GET.get('gallery_id'))

        return context


class ObjectSiteListView(ListView):
    model = ObjectSite

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Выбор квартир'
        return context


class ObjectSiteDetailView(DetailView):
    model = ObjectSite

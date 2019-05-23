from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import (ObjectGallery, ObjectGalleryImage)
from apps.realty.models.object_document import ObjectDocument

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
        context['object_info_tabs'] = ObjectInfoTab.objects.filter(object_id=self.get_object().pk)
        context['object_files'] = ObjectFile.objects.filter(object_id=self.get_object().pk)

        context['object_galleries'] = ObjectGallery.objects.filter(object=self.get_object().pk).order_by('-order')
        context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=context['object_galleries'].first())

        context['object_documents'] = ObjectDocument.objects.filter(object=self.get_object().pk).order_by('-updated')[:9]
        return context


class ObjectSiteListView(ListView):
    model = ObjectSite

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Выбор квартир'
        return context


class ObjectSiteDetailView(DetailView):
    model = ObjectSite


# Object gallery in json format
def object_gallery(request, gallery_id):
    gallery_images = ObjectGalleryImage.objects.filter(gallery=gallery_id).values('image',)
    gallery_images = list(gallery_images)
    return JsonResponse(gallery_images, safe=False)


def requestAjax(request, object_id):
    data = 'nothing'
    if request.is_ajax():
        # data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')
        data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')[:3]
        data = list(data)
    return JsonResponse(data, safe=False)

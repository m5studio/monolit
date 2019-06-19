from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage
from apps.realty.models.object_document import ObjectDocument
from apps.realty.models.object_video import ObjectVideo

from apps.news.models import News

from apps.realty.models.object_site_bathroom import ObjectBathroom
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_elevator import ObjectElevator

from django.db.models import Q


class ObjectListView(ListView):
    model = Object
    queryset = Object.objects.filter(active=True).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Объекты'
        context['objects_qty'] = Object.objects.filter(active=True).count()

        # TODO: write correct query
        # context['object_sites_qty'] = ObjectSite.objects.filter( Q(object_id=2) )
        context['object_sites_qty'] = ObjectSite.objects.filter( Q(object_id=2) )

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
        context['object_news'] = News.objects.filter(object=self.get_object().pk).order_by('-updated')
        context['other_objects'] = Object.objects.filter(active=True).exclude(id=self.get_object().pk).order_by('?')[:4]
        context['object_videos'] = ObjectVideo.objects.filter(object=self.get_object().pk)

        context['object_special_offers'] = ObjectSite.objects.filter(object=self.get_object().pk, active=True, special_offer=True).order_by('?')[:3]
        context['object_special_offers_qty'] = ObjectSite.objects.filter(object=self.get_object().pk, active=True, special_offer=True).count()

        # Object Documents Pagination
        context['object_documents'] = ObjectDocument.objects.filter(object=self.get_object().pk).order_by('-updated')
        paginator = Paginator(context['object_documents'], 9)
        page_docs = self.request.GET.get('page-docs')
        try:
            context['object_documents'] = paginator.page(page_docs)
        except PageNotAnInteger:
            context['object_documents'] = paginator.page(1)
        except EmptyPage:
            context['object_documents'] = paginator.page(paginator.num_pages)
        # END Object Documents Pagination

        return context


class ObjectSiteListView(ListView):
    model = ObjectSite
    queryset = ObjectSite.objects.filter(active=True).order_by('-updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Выбор квартир'
        return context


class ObjectSiteDetailView(DetailView):
    model = ObjectSite
    queryset = ObjectSite.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = '{rooms_qty} {site_type} №{site_number} в {object_type} «{object_name}»'.format(rooms_qty=self.get_object().get_rooms_qty_display(),
                                                                                                        site_type=self.get_object().get_site_type_display(),
                                                                                                        site_number=self.get_object().site_number,
                                                                                                        object_type=self.get_object().object.get_object_type_display(),
                                                                                                        object_name=self.get_object().object.name)
        # TODO: make more complicated and detailed query selection
        other_flats_query = ObjectSite.objects.filter(active=True, object=self.get_object().object.pk, rooms_qty=self.get_object().rooms_qty).exclude(id=self.get_object().pk)
        context['simular_flats'] = other_flats_query.order_by('?')[:3]
        context['simular_flats_count'] = other_flats_query.count()

        context['bathrooms'] = ObjectBathroom.objects.filter(object_site=self.get_object().pk)
        context['balconies'] = ObjectBalcony.objects.filter(object_site=self.get_object().pk)
        context['elevators'] = ObjectElevator.objects.filter(object_section=self.get_object().object_section.pk)

        return context


# Object gallery in json format
def object_gallery(request, gallery_id):
    gallery_images = ObjectGalleryImage.objects.filter(gallery=gallery_id).values('image',)
    gallery_images = list(gallery_images)
    return JsonResponse(gallery_images, safe=False)


# def requestAjax(request, object_id):
#     data = 'nothing'
#     if request.is_ajax():
#         # data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')
#         data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')[:9]
#         data = list(data)
#     return JsonResponse(data, safe=False)

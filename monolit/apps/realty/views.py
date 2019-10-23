import os
from django.conf import settings

from django.db.models import Count, Min, Max

from django.views.generic import ListView, DetailView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.core.classes.render_to_pdf import RenderToPDF

from apps.realty.models.object import Object
from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_info_tab import ObjectInfoTab
from apps.realty.models.object_file import ObjectFile
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage
from apps.realty.models.object_document import ObjectDocument
from apps.realty.models.object_video import ObjectVideo
from apps.realty.models.object_site_bathroom import ObjectBathroom
from apps.realty.models.object_site_balcony import ObjectBalcony
from apps.realty.models.object_elevator import ObjectElevator

from apps.news.models.news import News
from apps.mortgage.models import Offer


class ObjectListView(ListView):
    model = Object
    queryset = Object.objects.filter(active=True, all_sold=False).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Объекты'
        context['objects_qty'] = Object.objects.filter(active=True, all_sold=False).count()
        context['objects_sold'] = Object.objects.filter(active=True, all_sold=True).order_by('order')
        return context


class ObjectDetailView(DetailView):
    model = Object
    queryset = Object.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = Object._meta
        context['page_title'] = f'{self.get_object().name}'

        # if self.get_object().object_type:
        #     context['page_title'] = f'{self.get_object().get_object_type_display()} {self.get_object().name}'
        # context['page_meta_description'] = 'my custom meta'

        context['object_info_tabs'] = ObjectInfoTab.objects.filter(object_id=self.get_object().pk)
        context['object_files'] = ObjectFile.objects.filter(object_id=self.get_object().pk)
        context['object_galleries'] = ObjectGallery.objects.filter(object=self.get_object().pk).order_by('-order')
        context['object_galleries_images'] = ObjectGalleryImage.objects.filter(gallery__object=self.get_object().pk, gallery=context['object_galleries'].first())
        context['object_news'] = News.objects.filter(object=self.get_object().pk).order_by('-updated')
        context['other_objects'] = Object.objects.filter(active=True, all_sold=False).exclude(id=self.get_object().pk).order_by('?')[:4]
        context['object_videos'] = ObjectVideo.objects.filter(object=self.get_object().pk)

        context['object_special_offers'] = ObjectSite.objects.filter(object=self.get_object().pk, active=True, special_offer=True).order_by('?')[:3]
        context['object_special_offers_qty'] = ObjectSite.objects.filter(object=self.get_object().pk, active=True, special_offer=True).count()

        # ObjectDocument Pagination
        context['object_documents'] = ObjectDocument.objects.filter(object=self.get_object().pk).order_by('-updated')
        paginator = Paginator(context['object_documents'], 9)
        page_docs = self.request.GET.get('page-docs')
        try:
            context['object_documents'] = paginator.page(page_docs)
        except PageNotAnInteger:
            context['object_documents'] = paginator.page(1)
        except EmptyPage:
            context['object_documents'] = paginator.page(paginator.num_pages)
        # END ObjectDocument Pagination

        context['mortgage_offers'] = Offer.objects.filter(object=self.get_object().pk).order_by('rate_from')
        return context


class ObjectSiteListView(ListView):
    model = ObjectSite
    queryset = ObjectSite.objects.filter(active=True).order_by('-updated')
    paginate_by = 12
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Выбор квартир'
        return context


class ObjectSiteDetailView(DetailView):
    model = ObjectSite
    queryset = ObjectSite.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = ObjectSite._meta

        # context['page_title'] = self.model.flat_name_full(self)
        context['page_title'] = self.get_object().flat_name_full()
        # context['page_title'] = '{rooms_qty} {site_type} №{site_number} в {object_type} «{object_name}»'.format(rooms_qty=self.get_object().get_rooms_qty_display(),
        #                                                                                                         site_type=self.get_object().get_site_type_display(),
        #                                                                                                         site_number=self.get_object().site_number,
        #                                                                                                         object_type=self.get_object().object.object_type,
        #                                                                                                         object_name=self.get_object().object.name)

        # TODO: make more complicated and detailed query selection
        other_flats_query = ObjectSite.objects.filter(active=True, object=self.get_object().object.pk, rooms_qty=self.get_object().rooms_qty).exclude(id=self.get_object().pk)
        context['simular_flats'] = other_flats_query.order_by('?')[:3]
        context['simular_flats_count'] = other_flats_query.count()

        context['bathrooms'] = ObjectBathroom.objects.filter(object_site=self.get_object().pk)
        context['balconies'] = ObjectBalcony.objects.filter(object_site=self.get_object().pk)

        if self.get_object().object_section is not None:
            context['elevators'] = ObjectElevator.objects.filter(object_section=self.get_object().object_section.pk)

        context['mortgage_offers'] = Offer.objects.filter(object=self.get_object().object.pk).order_by('rate_from')
        return context


class ObjectSiteDetailViewPDF(View):
    def get(self, request, pk):
        object = ObjectSite.objects.filter(active=True).get(id=pk)
        filename = '[monolit.site] ' + getattr(object, 'site_type') + ' ID ' + getattr(object, 'crm_id')

        # Full path to Cirilic font
        path_to_static_dir = os.path.join(settings.BASE_DIR, 'static')
        path_to_fonts_dir = os.path.join(path_to_static_dir, 'fonts')
        path_to_font = os.path.join(path_to_fonts_dir, 'roboto_regular.ttf')

        # Full path to Monolit logo
        path_to_images_dir = os.path.join(path_to_static_dir, 'images')
        path_to_monolit_logo = os.path.join(path_to_images_dir, 'monolit-logo-text.png')

        context = {
            'font_path': path_to_font,
            'monolit_logo': path_to_monolit_logo,
            'object': object,
            'request': request
        }
        return RenderToPDF.render('pdf/objectsite_detail_pdf.html', context, filename)

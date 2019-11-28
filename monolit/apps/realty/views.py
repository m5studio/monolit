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

from apps.realty.models.object_commercial import ObjectCommercial
from apps.realty.models.object_commercial_site import ObjectCommercialSite

from apps.news.models.news import News
from apps.mortgage.models import Offer


class ObjectListView(ListView):
    model = Object
    queryset = Object.objects.filter(active=True, all_sold=False).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Жилые объекты'
        context['objects_qty'] = Object.objects.filter(active=True, all_sold=False).count()
        context['objects_sold'] = Object.objects.filter(active=True, all_sold=True).order_by('order')
        return context


class ObjectDetailView(DetailView):
    model = Object
    queryset = Object.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = Object._meta
        context['page_title'] = f'{self.get_object().display_name()}'
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
        context['page_title'] = 'Выбор жилой недвижимости'
        return context


class ObjectSiteDetailView(DetailView):
    model = ObjectSite
    queryset = ObjectSite.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = ObjectSite._meta
        context['page_title'] = self.get_object().display_name_full()
        # TODO: make more complicated and detailed query selection
        other_sites_query = ObjectSite.objects.filter(active=True, object=self.get_object().object.pk, rooms_qty=self.get_object().rooms_qty).exclude(id=self.get_object().pk)
        context['simular_sites'] = other_sites_query.order_by('?')[:3]
        context['simular_sites_count'] = other_sites_query.count()
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
            'page_title': object.display_name_full(),
            'font_path': path_to_font,
            'monolit_logo': path_to_monolit_logo,
            'object': object,
            'request': request,
        }
        return RenderToPDF.render('pdf/object_site_detail_pdf.html', context, filename)


class ObjectCommercialListView(ListView):
    model = ObjectCommercial
    queryset = ObjectCommercial.objects.filter(active=True, all_sold=False).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Коммерческие Объекты'
        context['objects_commercial_qty'] = ObjectCommercial.objects.filter(active=True, all_sold=False).count()
        context['objects_commercial_sold'] = ObjectCommercial.objects.filter(active=True, all_sold=True).order_by('order')
        return context


class ObjectCommercialDetailView(DetailView):
    model = ObjectCommercial
    queryset = ObjectCommercial.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = ObjectCommercial._meta
        context['page_title'] = f'{self.get_object().display_name()}'
        return context


class ObjectCommercialSiteListView(ListView):
    model = ObjectCommercialSite
    queryset = ObjectCommercialSite.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Выбор коммерческой недвижимости'
        return context


class ObjectCommercialSiteDetailView(DetailView):
    model = ObjectCommercialSite
    queryset = ObjectCommercialSite.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opts'] = ObjectCommercialSite._meta
        context['page_title'] = self.get_object().display_name_full()
        return context


class ObjectCommercialSiteDetailViewPDF(View):
    def get(self, request, pk):
        object = ObjectCommercialSite.objects.filter(active=True).get(id=pk)
        filename = '[monolit.site] ' + getattr(object, 'site_type') + ' ID ' + getattr(object, 'crm_id')

        # Full path to Cirilic font
        path_to_static_dir = os.path.join(settings.BASE_DIR, 'static')
        path_to_fonts_dir = os.path.join(path_to_static_dir, 'fonts')
        path_to_font = os.path.join(path_to_fonts_dir, 'roboto_regular.ttf')

        # Full path to Monolit logo
        path_to_images_dir = os.path.join(path_to_static_dir, 'images')
        path_to_monolit_logo = os.path.join(path_to_images_dir, 'monolit-logo-text.png')

        context = {
            'page_title': object.display_name_full(),
            'font_path': path_to_font,
            'monolit_logo': path_to_monolit_logo,
            'object': object,
            'request': request,
        }
        return RenderToPDF.render('pdf/object_commercial_site_detail_pdf.html', context, filename)

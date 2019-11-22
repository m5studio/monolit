# from django.shortcuts import render
from django.http import JsonResponse

from apps.realty.models.object_site import ObjectSite
from apps.realty.models.object_commercial_site import ObjectCommercialSite
from apps.realty.models.object_gallery import ObjectGallery, ObjectGalleryImage

from apps.mortgage.models import Offer
from apps.company.models.tender import Tender, TenderFile


def mergeTwoDicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

# API for ObjectSite all
def api_object_sites_all(request):
    object_sites = ObjectSite.objects.filter(active=True).values('id', 'crm_id')
    object_sites_list = list(object_sites)
    return JsonResponse(object_sites_list, safe=False)

# API for ObjectSite info related to Object
def api_object_sites_info(request, object_id):
    object_sites = ObjectSite.objects
    object_sites_info = object_sites.object_sites_info_aggregated(object_id)

    room_0 = object_sites.sites_info_aggregated(object_id, 0)
    room_1 = object_sites.sites_info_aggregated(object_id, 1)
    room_2 = object_sites.sites_info_aggregated(object_id, 2)
    room_3 = object_sites.sites_info_aggregated(object_id, 3)
    room_4 = object_sites.sites_info_aggregated(object_id, 4)

    sites_info = list()
    sites_info.extend([object_sites_info,
                        {'sites_info': [
                                mergeTwoDicts({'name': 'Ст', 'rooms': 0}, room_0),
                                mergeTwoDicts({'name': '1',  'rooms': 1}, room_1),
                                mergeTwoDicts({'name': '2',  'rooms': 2}, room_2),
                                mergeTwoDicts({'name': '3',  'rooms': 3}, room_3),
                                mergeTwoDicts({'name': '4+', 'rooms': 4}, room_4),
                            ]
                        }])
    return JsonResponse(sites_info, safe=False)

# API for ObjectSite
def api_object_site(request, site_id):
    site_info = ObjectSite.objects.filter(id=site_id, active=True).values('crm_id', 'site_type', 'price_total')
    site_info = list(site_info)
    return JsonResponse(site_info, safe=False)

# API for ObjectCommercialSite info related to ObjectCommercial
def api_object_commercial_sites_info(request, object_commercial_id):
    object_commercial_sites = ObjectCommercialSite.objects
    object_commercial_sites_info = object_commercial_sites.object_sites_info_aggregated(object_commercial_id)

    sites_commercial_info = list()
    sites_commercial_info.extend([object_commercial_sites_info,
                                    {'sites_info': [
                                            'TODO',
                                            'TODO',
                                        ]
                                    }])
    return JsonResponse(sites_commercial_info, safe=False)

# API for ObjectGallery
def api_object_gallery(request, gallery_id):
    gallery_images = ObjectGalleryImage.objects.filter(gallery=gallery_id).values('image')
    gallery_images_list = list(gallery_images)
    return JsonResponse(gallery_images_list, safe=False)

# API for Mortgage Offer
def api_mortgage_offer(request, offer_id):
    mortgage_offer = Offer.objects.filter(id=offer_id).values('id', 'first_payment_from', 'first_payment_to', 'loan_term_from', 'loan_term_to', 'rate_from', 'rate_to')
    mortgage_offer = list(mortgage_offer)
    return JsonResponse(mortgage_offer, safe=False)


"""
def requestAjax(request, object_id):
    data = 'nothing'
    if request.is_ajax():
        # data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')
        data = ObjectDocument.objects.filter(object=object_id).values('title', 'author__name', 'date', 'file')[:9]
        data = list(data)
    return JsonResponse(data, safe=False)
"""

from django.urls import path, include

from apps.api.views import (
    api_object_gallery,
    api_object_sites_all,
    api_object_sites_info,
    api_object_site,
    api_mortgage_offer,

    # requestAjax
)


app_name = 'api'

urlpatterns = [
    path('api/', include([
        path('object-gallery/<int:gallery_id>/', api_object_gallery, name='object-gallery'),
        path('object-sites-all/', api_object_sites_all, name='object-sites-all'),
        path('object-sites-info/<int:object_id>/', api_object_sites_info, name='object-sites-info'),
        path('site/<int:site_id>/', api_object_site, name='site-info'),
        path('mortgage-offer/<int:offer_id>/', api_mortgage_offer, name='mortgage-offer'),
    ])),

    # path('object-docs/<int:object_id>/', requestAjax, name='docs')
]

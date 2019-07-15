from django.urls import path, include

from apps.api.views import (
    api_object_gallery,
    api_object_sites_info,

    # requestAjax
)


app_name = 'api'

urlpatterns = [
    path('api/', include([
        path('object-gallery/<int:gallery_id>/', api_object_gallery, name='object-gallery'),
        path('object/<int:object_id>/sites-info/', api_object_sites_info, name='object-sites-info'),
    ])),

    # path('object-docs/<int:object_id>/', requestAjax, name='docs')
]

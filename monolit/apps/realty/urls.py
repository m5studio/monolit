from django.urls import path, include

from apps.realty.views import (
    ObjectListView,
    ObjectDetailView,

    ObjectSiteListView,
    ObjectSiteDetailView,

    json_object_gallery,
    json_object_sites_info,
    # requestAjax
)


app_name = 'object'

urlpatterns = [
    path('objects/', include([
        path('', ObjectListView.as_view(), name='list'),
        path('<slug:slug>/', ObjectDetailView.as_view(), name='detail')
    ])),

    path('sites/', include([
        path('', ObjectSiteListView.as_view(), name='site-list'),
        path('<int:pk>/', ObjectSiteDetailView.as_view(), name='site-detail')
    ])),

    path('json/object-gallery/<int:gallery_id>/', json_object_gallery, name='json-gallery'),
    path('json/object/<int:object_id>/sites-info/', json_object_sites_info, name='json-object-sites-info'),

    # path('object-docs/<int:object_id>/', requestAjax, name='docs')
]

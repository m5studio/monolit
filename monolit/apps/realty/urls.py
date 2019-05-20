from django.urls import path, include

from apps.realty.views import (
    ObjectListView,
    ObjectDetailView,

    ObjectSiteListView,
    ObjectSiteDetailView,

    object_gallery
)


urlpatterns = [
    path('objects/', include([
        path('', ObjectListView.as_view(), name='objects-list'),
        path('<slug:slug>/', ObjectDetailView.as_view(), name='object-detail')
    ])),

    path('sites/', include([
        path('', ObjectSiteListView.as_view(), name='objects-sites-list'),
        path('<int:pk>/', ObjectSiteDetailView.as_view(), name='object-site-detail')
    ])),

    path('object-gallery/<int:gallery_id>/', object_gallery, name='object-gallery'),
]

from django.urls import path, include

from apps.realty.views import (
    ObjectListView,
    ObjectDetailView,

    ObjectSiteListView,
    ObjectSiteDetailView,

    gallery_content
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

    # path('gallery-obj/', gallery_content),
    path('object-gal/<int:gallery_id>/', gallery_content),
    # path('gallery-obj/<int:object_id>/<int:gallery_id>/', gallery_content)
]

from django.urls import path, include

from apps.realty.views import (
    ObjectListView,
    ObjectDetailView,

    ObjectSiteListView,
    ObjectSiteDetailView,

    ObjectSiteDetailViewPDF,
)


app_name = 'object'

urlpatterns = [
    path('objects/', include([
        path('', ObjectListView.as_view(), name='list'),
        path('<slug:slug>/', ObjectDetailView.as_view(), name='detail')
    ])),

    path('sites/', include([
        path('', ObjectSiteListView.as_view(), name='site-list'),
        path('<int:pk>/', ObjectSiteDetailView.as_view(), name='site-detail'),
        path('<int:pk>/pdf/', ObjectSiteDetailViewPDF.as_view(), name='site-detail-pdf')
    ])),
]

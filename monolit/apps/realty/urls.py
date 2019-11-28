from django.urls import path, include

from apps.realty.views import (
    ObjectListView,
    ObjectDetailView,

    ObjectSiteListView,
    ObjectSiteDetailView,
    ObjectSiteDetailViewPDF,


    ObjectCommercialListView,
    ObjectCommercialDetailView,

    ObjectCommercialSiteListView,
    ObjectCommercialSiteDetailView,
    ObjectCommercialSiteDetailViewPDF,
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
        path('<int:pk>/pdf/', ObjectSiteDetailViewPDF.as_view(), name='site-detail-pdf'),
    ])),

    path('objects-commercial/', include([
        path('', ObjectCommercialListView.as_view(), name='commercial-list'),
        path('<slug:slug>/', ObjectCommercialDetailView.as_view(), name='commercial-detail')
    ])),

    path('sites-commercial/', include([
        path('', ObjectCommercialSiteListView.as_view(), name='site-commercial-list'),
        path('<int:pk>/', ObjectCommercialSiteDetailView.as_view(), name='site-commercial-detail'),
        path('<int:pk>/pdf/', ObjectCommercialSiteDetailViewPDF.as_view(), name='site-commercial-detail-pdf'),
    ])),
]

from django.urls import path

from apps.core.views import (
                                HomepageView,
                                FavoritesView,
                            )


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('favorites/', FavoritesView.as_view(), name='favorites' )
]

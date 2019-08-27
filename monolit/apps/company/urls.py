from django.urls import path, include

from apps.company.views import (
    CompanyView,
)


app_name = 'company'

urlpatterns = [
    path('company/', include([
        path('', CompanyView.as_view(), name='company'),
        # path('<int:pk>/', NewsDetailView.as_view(), name='detail')
    ])),
]

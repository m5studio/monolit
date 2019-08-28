from django.urls import path, include

from apps.company.views import (
    CompanyView,
    CompanyMissionView,
    CompanyManagementView,
    CompanyResponsibilityView,
    CompanyJobView,
)


app_name = 'company'

urlpatterns = [
    path('company/', include([
        path('', CompanyView.as_view(), name='company'),
        path('mission/', CompanyMissionView.as_view(), name='mission'),
        path('management/', CompanyManagementView.as_view(), name='management'),
        path('responsibility/', CompanyResponsibilityView.as_view(), name='responsibility'),
        path('job/', CompanyJobView.as_view(), name='job'),
    ])),
]

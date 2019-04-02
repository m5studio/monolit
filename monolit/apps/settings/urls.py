from django.urls import path
from apps.settings.views import HomepageView


urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
]

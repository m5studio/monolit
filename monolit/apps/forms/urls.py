from django.urls import path, include
from .views import callback_form


app_name = 'forms'

urlpatterns = [
    path('forms/', include([
        path('callback/', callback_form, name="callback"),
    ])),
]

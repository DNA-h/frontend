from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import RegisterView

urlpatterns = [
    url(r'^registration/$', RegisterView.as_view(), name='rest_register'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", TemplateView.as_view(),
        name="account_confirm_email"),
]

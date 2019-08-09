from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import RegisterView ,LoginView

urlpatterns = [
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", TemplateView.as_view(),
        name="account_confirm_email"),
    url(r'^login/$', LoginView.as_view(), name='login'),

]

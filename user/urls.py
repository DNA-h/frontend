from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import RegisterView, LoginView, VerifyEmailView

urlpatterns = [
    url(r'^registration/$', RegisterView.as_view(), name='registration'),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", VerifyEmailView,
        name="account_confirm_email"),
    url(r'^login/$', LoginView.as_view(), name='login'),

]

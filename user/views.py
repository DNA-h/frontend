from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from allauth.account import app_settings as auth_settings
from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from rest_auth.models import TokenModel
from rest_auth.utils import jwt_encode
from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes

from user.utils import complete_signup

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)

class HomePageView(TemplateView):
    template_name = "index.html"


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if auth_settings.EMAIL_VERIFICATION == \
                auth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": _("Verification e-mail sent.")}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }

            return JWTSerializer(data).data
        else:
            return TokenSerializer(user.auth_token).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user,
                        auth_settings.EMAIL_VERIFICATION,
                        None)
        return user


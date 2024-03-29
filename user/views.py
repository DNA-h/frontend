import datetime
from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.conf import settings
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import status
from allauth.account import app_settings as auth_settings
from allauth.account.models import EmailConfirmation, EmailAddress, EmailConfirmationHMAC
from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from rest_auth.models import TokenModel
from rest_auth.registration.app_settings import RegisterSerializer, register_permission_classes
from user.models import User
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
        return TokenSerializer(user.auth_token).data



    def create(self, request, *args, **kwargs):
        try:
            _user = User.objects.get(username=self.request.data['username']
                                , email=self.request.data['email'])
        except:
            _user = None
        try:
            verified = EmailAddress.objects.get(email=request.data['email']).verified
        except:
            verified = None
        a=False
        if _user and settings.ACCOUNT_LOGIN_BY_MAIL:
            if auth_settings.EMAIL_VERIFICATION == \
                    auth_settings.EmailVerificationMethod.MANDATORY\
                    and not verified:
                a = True
            else:
                user = _user
                self.create_new_token(user)
                headers = {}
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        if a:
            return Response("You need to confirm email",
                            status=status.HTTP_200_OK)
        else:
            return Response(self.get_response_data(user),
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer):

        user = serializer.save(self.request)
        create_token(self.token_model, user, serializer)
        complete_signup(self.request._request, user,
                        auth_settings.EMAIL_VERIFICATION,
                        None)
        return user

    def create_new_token(self,user):
        try:
            Token.objects.get(user=user).delete()
        except:
            pass
        create_token(self.token_model, user , None)


def VerifyEmailView(request, *args, **kwargs):
    emailadresses = EmailAddress.objects.all()
    for emailadress in emailadresses:
        emailconfirmation = EmailConfirmation.objects.\
            get(email_address=emailadress)
        sent_date = emailconfirmation.sent.date()
        now = datetime.datetime.now().date()
        diff = now - sent_date
        if diff.days <= settings.ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS:
            if emailconfirmation.key == kwargs['key'].lower():
                if not emailadress.verified:
                    emailadress.verified = True
                    emailadress.save()
            return Response("Your account is active, go to login page",
                            status=status.HTTP_200_OK)
        elif emailadress.verified:
            return Response("Your account was active, go to login page",
                            status=status.HTTP_200_OK)
            # return redirect('http://127.0.0.1:8001/admin/')

        else:
            return Response("Your link for activation is expired, go to signup page",
                            status=status.HTTP_200_OK)





class LoginView(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def get_response_serializer(self):
        response_serializer = TokenSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token = create_token(self.token_model, self.user,
                                      self.serializer)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()
        serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        check = self.serializer.is_valid(raise_exception=True)
        if check:
            if auth_settings.EMAIL_VERIFICATION == \
                    auth_settings.EmailVerificationMethod.MANDATORY:
                    verified = EmailConfirmation.objects.get(email_address = request.data['email'])
                    if not verified:
                        return "You need to confirm email"
        self.login()
        return self.get_response()
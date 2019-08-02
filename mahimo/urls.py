"""mahimo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import questionnaire
from clients.view import HomePageView
from questionnaire.views import *
admin.autodiscover()

# from crm.models import Client

admin.site.site_header = "Mahimo Admin"
admin.site.site_title = "Mahimo Admin Portal"
admin.site.index_title = "Welcome to Mahimo Portal"

schema_view = get_schema_view(
    openapi.Info(
        title="Mahimo API",
        default_version="v1",
        description="Mahimo API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@mahimo.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class ClientSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Client
#         fields = ('slug', 'bio', 'address', 'birth_date')
#
#
# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'clients', ClientViewSet)

urlpatterns = [
    url(r"^docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(
        cache_timeout=0), name="schema-json"),
    url(r"^docs/$", schema_view.with_ui("swagger",
                                        cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    url(r'^accounts/', include('allauth.urls')),
    # url(r"^crm/"/, include("crm.urls")),
    # url(r"^clinic/", include("clinic.urls")),
    url(r"^q/", include("questionnaire.urls")),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r"^", include(router.urls)),
    # url(r"^accounts/",
    #     include("rest_framework.urls", namespace="rest_framework")),

    path('',HomePageView.as_view(),name="home"),
]

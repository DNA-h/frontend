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
from rest_framework import routers, serializers, viewsets, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from user.views import HomePageView
from questionnaire.views import *
admin.autodiscover()

# from crm.models import Client

admin.site.site_header = "Mahimo Admin"
admin.site.site_title = "Mahimo Admin Portal"
admin.site.index_title = "Welcome to Mahimo Portal"


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path(r"q/", include("questionnaire.urls")),
    path('', HomePageView.as_view(), name="home"),
    path(r'', include('user.urls')),
]

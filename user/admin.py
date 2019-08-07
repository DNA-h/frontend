from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token

from .models import *

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    list_display = ['username','email','is_active','key','token']

    def _token(self,obj):
        token = Token.objects.get(id = obj.id)
        return token
    _token.short_description = 'token1'
#
# admin.site.register(User, UserAdmin)

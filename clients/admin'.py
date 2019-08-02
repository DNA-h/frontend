from django.contrib import admin
from clients.models import User
from django.contrib.auth.admin import UserAdmin

#
# @admin.register(User)
# class UserAdmin (admin.ModelAdmin):
#     list_display = ('fist_name','last_name',)
#
#


admin.site.register(User,UserAdmin)

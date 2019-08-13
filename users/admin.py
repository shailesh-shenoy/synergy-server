"""Models related to users are registered on the admin site here"""
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(User, CustomUserAdmin)

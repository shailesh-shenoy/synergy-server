"""Models related to users are registered on the admin site here"""
from django.contrib import admin

from .models import User

admin.site.register(User)

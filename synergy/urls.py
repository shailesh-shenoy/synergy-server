"""Root level URLs are defined here"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework_social_oauth2.urls")),
    path("", views.api_root),
    path("", include("todos.urls")),
    path("", include("users.urls")),
]

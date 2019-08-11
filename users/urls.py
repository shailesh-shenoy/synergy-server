"""URLs related to users are defined here"""
from rest_framework import routers
from django.urls import include, path

from .views import UserViewSet, GroupViewSet, PermissionViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, "user")
router.register(r"groups", GroupViewSet, "group")
router.register(r"permissions", PermissionViewSet, "permission")

urlpatterns = [path("", include((router.urls, "users"), namespace="users"))]

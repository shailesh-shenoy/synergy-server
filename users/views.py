"""Views related to users are defined here"""
from rest_framework import viewsets
from django.contrib.auth.models import Group, Permission

from .serializers import UserSerializer, GroupSerializer, PermissionSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """Class to implement User API"""

    serializer_class = UserSerializer
    lookup_field = "username"
    queryset = User.objects.all().order_by("date_joined")


class GroupViewSet(viewsets.ModelViewSet):
    """Class to implement Group API"""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    """Class to implement Permission API"""

    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

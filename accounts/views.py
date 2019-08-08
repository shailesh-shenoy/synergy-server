from rest_framework import viewsets
from django.contrib.auth.models import User, Permission, Group

from .serializers import (
    AccountSerializer,
    UserSerializer,
    PermissionSerializer,
    GroupSerializer,
)
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all().order_by("id")


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("id")


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all().order_by("id")


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all().order_by("id")

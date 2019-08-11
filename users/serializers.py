"""Serializers related to Users are defined here."""
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission

from .models import User
from todos.models import Todo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class to serialize the User API"""

    url = serializers.HyperlinkedIdentityField(
        view_name="users:user-detail", lookup_field="username"
    )
    groups = serializers.HyperlinkedRelatedField(
        view_name="users:group-detail", many=True, queryset=Group.objects.all()
    )
    user_permissions = serializers.HyperlinkedRelatedField(
        view_name="users:permission-detail",
        many=True,
        queryset=Permission.objects.all(),
    )
    todos = serializers.HyperlinkedRelatedField(
        view_name="todos:todo-detail", many=True, queryset=Todo.objects.all()
    )

    class Meta:
        model = User
        fields = (
            "id",
            "url",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "groups",
            "user_permissions",
            "todos",
            "last_login",
            "date_joined",
            "is_active",
        )
        read_only_fields = ("pk", "url", "last_login", "date_joined")
        extra_kwargs = {"password": {"write_only": True}}


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Class to serialize the Groups API"""

    url = serializers.HyperlinkedIdentityField(view_name="users:group-detail")
    permissions = serializers.HyperlinkedRelatedField(
        view_name="users:permission-detail",
        many=True,
        queryset=Permission.objects.all(),
    )

    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    """Class to serialize the Groups API"""

    url = serializers.HyperlinkedIdentityField(view_name="users:permission-detail")

    class Meta:
        model = Permission
        exclude = ("content_type",)

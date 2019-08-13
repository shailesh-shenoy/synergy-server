"""Serializers related to Users are defined here."""
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission

from todos.models import Todo
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Class to serialize the User API"""

    url = serializers.HyperlinkedIdentityField(
        view_name="users:user-detail", lookup_field="username"
    )
    groups = serializers.HyperlinkedRelatedField(
        view_name="users:group-detail", many=True, read_only=True
    )
    user_permissions = serializers.HyperlinkedRelatedField(
        view_name="users:permission-detail", many=True, read_only=True
    )
    todos = serializers.HyperlinkedRelatedField(
        view_name="todos:todo-detail", many=True, read_only=True
    )

    def create(self, validated_data):
        """Create a user instance from serializer fields"""
        user = User(username=validated_data.get("username", None))
        user.set_password(validated_data.get("password", None))
        for field in validated_data:
            if field == "password" or field == "username":
                pass
            else:
                user.__setattr__(field, validated_data.get(field))
        user.save()
        return user

    def update(self, instance, validated_data):
        """Updates the serializer fields"""
        for field in validated_data:
            if field == "password":
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

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
            "preferred_theme",
        )
        read_only_fields = (
            "pk",
            "url",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
            "todos",
            "is_active",
        )
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

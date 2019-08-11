"""Serializers related to Todos are defined here."""
from rest_framework import serializers

from .models import Todo
from users.models import User


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    """Class to serialize the todos API"""

    url = serializers.HyperlinkedIdentityField(view_name="todos:todo-detail")
    user = serializers.HyperlinkedRelatedField(
        view_name="users:user-detail",
        lookup_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Todo
        fields = (
            "pk",
            "url",
            "user",
            "title",
            "description",
            "has_deadline",
            "due_date",
            "completed",
        )
        read_only_fields = ("pk", "url")

    def validate(self, data):

        """Function to ensure that due_date is null when has_deadline is false
        and due_date is entered when has_deadline is true
        """
        if data["has_deadline"] == False:
            if data["due_date"] is not None:
                raise serializers.ValidationError(
                    "due_date must be null when has_deadline is False"
                )
        else:
            if data["due_date"] is None:
                raise serializers.ValidationError(
                    "due_date must be entered when has_deadline is True"
                )
        return data

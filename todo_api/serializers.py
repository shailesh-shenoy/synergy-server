from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "pk",
            "url",
            "title",
            "description",
            "has_deadline",
            "due_date",
            "completed",
        )
        read_only_fields = ("pk", "url")

    def validate(self, data):

        # Check that due_date is null when has_deadline is false
        # And due_date is entered when has_deadline is true
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


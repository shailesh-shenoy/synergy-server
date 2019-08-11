"""Views related to Todos are defined here"""
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """ViewSet to implement Todo API"""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all().order_by("id")

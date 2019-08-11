"""URLs related to todos defined here"""
from rest_framework import routers
from django.urls import include, path

from . import views

router = routers.SimpleRouter()
router.register(r"todos", views.TodoViewSet, "todo")

urlpatterns = [path("", include((router.urls, "todos"), namespace="todos"))]

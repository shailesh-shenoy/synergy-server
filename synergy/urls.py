from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo_api import views as todo_views
from accounts import views as account_views

router = routers.DefaultRouter()
router.register(r"todos", todo_views.TodoViewSet, "todo")
router.register(r"accounts", account_views.AccountViewSet, "account")
router.register(r"users", account_views.UserViewSet, "user")
router.register(r"permissions", account_views.PermissionViewSet, "permission")
router.register(r"groups", account_views.GroupViewSet, "group")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", include("rest_framework_social_oauth2.urls")),
]

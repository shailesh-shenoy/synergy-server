"""Root level views are defined here"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request):
    """View to implement the api root"""
    return Response(
        {
            "users": reverse("users:user-list", request=request),
            "todos": reverse("todos:todo-list", request=request),
        }
    )

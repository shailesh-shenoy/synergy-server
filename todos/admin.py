"""Todo models are registered to admin here."""
from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """Class to define fields displayed in admin"""

    list_display = (
        "pk",
        "user",
        "title",
        "description",
        "has_deadline",
        "due_date",
        "completed",
    )


# Register your models here.
admin.site.register(Todo, TodoAdmin)

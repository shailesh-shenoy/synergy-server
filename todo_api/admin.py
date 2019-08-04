from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "description",
        "has_deadline",
        "due_date",
        "completed",
    )


# Register your models here.
admin.site.register(Todo, TodoAdmin)

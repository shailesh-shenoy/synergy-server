"""Models related to Todos are defined here."""
from django.db import models

from users.models import User


class Todo(models.Model):
    """Class to define the Todo model"""

    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
    title = models.CharField("Todo", max_length=120)
    description = models.TextField("Description")
    creation_date = models.DateTimeField("Created on", auto_now_add=True)
    has_deadline = models.BooleanField("Has Deadline", default=False)
    due_date = models.DateTimeField("Deadline", null=True, blank=True)
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.title

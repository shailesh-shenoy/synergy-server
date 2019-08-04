from django.db import models


class Todo(models.Model):
    title = models.CharField("Todo", max_length=120)
    description = models.TextField("Description")
    has_deadline = models.BooleanField("Has Deadline", default=False)
    due_date = models.DateTimeField("Deadline", null=True, blank=True)
    completed = models.BooleanField("Completed", default=False)

    def __str__(self):
        return self.title

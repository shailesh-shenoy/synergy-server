from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    DARK = "dark"
    LIGHT = "light"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_theme = models.CharField(
        "Preferred Theme",
        max_length=10,
        choices=((DARK, "Dark"), (LIGHT, "Light")),
        default=LIGHT,
    )

    def __str__(self):
        return self.user.username

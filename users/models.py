"""Models related to users are defined here."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User Model corresponding to users in DB"""

    DARK = "dark"
    LIGHT = "light"
    THEME_CHOICES = [(DARK, "Dark"), (LIGHT, "Light")]

    preferred_theme = models.CharField(
        "Preferred Theme", max_length=10, choices=THEME_CHOICES, default=LIGHT
    )


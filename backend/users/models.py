from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Custom user model extending Django's AbstractUser."""

    phone = models.CharField(
        _("phone number"),
        max_length=15,
        blank=True,
        null=True,
        help_text=_("Optional. Include country code (e.g. +1...)."),
    )
    address = models.TextField(
        _("address"),
        blank=True,
        null=True,
        help_text=_("Optional. User's primary address."),
    )

    def __str__(self):
        return self.username or self.email

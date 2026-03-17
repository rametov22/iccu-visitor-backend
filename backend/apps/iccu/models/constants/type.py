from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ("Type",)


class Type(models.TextChoices):
    LINK = "link", _("Ссылка")
    INFO = "info", _("Информация")

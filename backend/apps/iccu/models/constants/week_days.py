from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ("WeekDays",)


class WeekDays(models.IntegerChoices):
    MONDAY = 1, _("Понедельник")
    TUESDAY = 2, _("Вторник")
    WEDNESDAY = 3, _("Среда")
    THURSDAY = 4, _("Четверг")
    FRIDAY = 5, _("Пятница")
    SATURDAY = 6, _("Суббота")
    SUNDAY = 7, _("Воскресенье")

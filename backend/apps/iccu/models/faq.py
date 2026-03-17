from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ("FAQ",)


class FAQ(models.Model):
    question = models.CharField(_("Вопрос"), max_length=500)
    answer = models.TextField(_("Ответ"))
    order = models.PositiveSmallIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активно"), default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Часто задаваемый вопрос")
        verbose_name_plural = _("Часто задаваемые вопросы (ЧЗВ)")

    def __str__(self):
        return self.question[:80]

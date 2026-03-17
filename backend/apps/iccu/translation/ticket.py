from modeltranslation.translator import TranslationOptions, register

from ..models import TicketSource

__all__ = ("TicketSourceTranslationOptions",)


@register(TicketSource)
class TicketSourceTranslationOptions(TranslationOptions):
    fields = ("description",)

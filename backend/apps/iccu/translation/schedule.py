from modeltranslation.translator import TranslationOptions, register

from ..models import Schedule


@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ("note",)

from modeltranslation.translator import TranslationOptions, register

from ..models import Complex, Place


@register(Complex)
class ComplexTranslationOptions(TranslationOptions):
    fields = ("title", "orienteer")


@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ("name", "full_name")

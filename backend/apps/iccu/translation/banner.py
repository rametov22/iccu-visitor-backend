from modeltranslation.translator import TranslationOptions, register

from ..models import Banner

__all__ = ("BannerTranslationOptions",)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "city",
        "country",
    )

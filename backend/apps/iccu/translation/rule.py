from modeltranslation.translator import TranslationOptions, register

from ..models import Rule, RuleCategory


@register(RuleCategory)
class RuleCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Rule)
class RuleTranslationOptions(TranslationOptions):
    fields = ("text",)

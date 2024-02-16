from .models import Preparation
from modeltranslation.translator import register, TranslationOptions


@register(Preparation)
class PreparationTranslationOptions(TranslationOptions):
    fields = ('name', 'text')

from .models import UmraDuo
from modeltranslation.translator import register, TranslationOptions


@register(UmraDuo)
class UmraDuoTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

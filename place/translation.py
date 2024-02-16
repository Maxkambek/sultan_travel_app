from .models import Place
from modeltranslation.translator import register, TranslationOptions


@register(Place)
class PlaceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

from .models import Handbook
from modeltranslation.translator import register, TranslationOptions


@register(Handbook)
class HandbookTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'some_text')

from .models import News, Tour, Phone
from modeltranslation.translator import register, TranslationOptions


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Phone)
class PhoneTranslationOptions(TranslationOptions):
    fields = ('branch_name',)

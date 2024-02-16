from django.contrib import admin
from .models import Handbook
from modeltranslation.admin import TranslationAdmin


@admin.register(Handbook)
class HandbookAdmin(TranslationAdmin):
    list_display = ('name', 'id')

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

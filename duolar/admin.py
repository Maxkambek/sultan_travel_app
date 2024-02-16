from django.contrib import admin
from .models import UmraDuo
from modeltranslation.admin import TranslationAdmin


@admin.register(UmraDuo)
class UmraDuoNameAdmin(TranslationAdmin):
    list_display = ('id', 'name')

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

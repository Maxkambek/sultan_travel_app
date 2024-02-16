from django.contrib import admin
from .models import Place
from django.conf import settings
from modeltranslation.admin import TranslationAdmin


class PlaceAdmin(TranslationAdmin):
    list_display = ['id', 'name']

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': (
                    'css/admin/location_picker.css', 'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
                    'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
                    'modeltranslation/js/tabbed_translation_fields.js',),

            }
            js = ('https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                  'js/admin/location_picker.js', 'modeltranslation/css/tabbed_translation_fields.css',)


admin.site.register(Place, PlaceAdmin)

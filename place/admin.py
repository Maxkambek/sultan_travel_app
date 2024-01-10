from django.contrib import admin
from .models import Place
from django.conf import settings


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = ('https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                  'js/admin/location_picker.js',)


admin.site.register(Place, PlaceAdmin)

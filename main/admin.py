from django.contrib import admin
from .models import News, Tour

admin.site.register(News)


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass

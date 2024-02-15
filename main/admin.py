from django.contrib import admin
from .models import News, Tour, Phone


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass

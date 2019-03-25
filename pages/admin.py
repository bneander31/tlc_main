from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_name', 'active', 'publish_date']
    list_display_links = ('id', 'location_name')
    list_filter = ('location_name',)
    list_editable = ('active',)
    search_fields = ('location_name',)
    list_per_page = 25

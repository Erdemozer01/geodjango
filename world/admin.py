from django.contrib import admin
from .models import WorldBorder
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

@admin.register(WorldBorder)
class WorldBorderAdmin(LeafletGeoAdmin):
    list_display = ('name', "area", "lon", "lat")


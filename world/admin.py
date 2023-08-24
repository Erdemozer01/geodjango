from django.contrib import admin
from .models import WorldBorder, Zipcode
from leaflet.admin import LeafletGeoAdmin


# Register your models here.

@admin.register(WorldBorder)
class WorldBorderAdmin(LeafletGeoAdmin):
    list_display = ('name', "area", "lon", "lat")


@admin.register(Zipcode)
class ZipcodeAdmin(LeafletGeoAdmin):
    list_display = ('code', "poly")

from django.contrib.gis import admin
from .models import WorldBorder, Zipcode
from leaflet.admin import LeafletGeoAdmin


# Register your models here.

@admin.register(WorldBorder)
class WorldBorderAdmin(admin.GISModelAdmin):
    list_display = ('name', "area", "lon", "lat")


@admin.register(Zipcode)
class ZipcodeAdmin(admin.GISModelAdmin):
    list_display = ('code', "poly")

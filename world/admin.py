from django.contrib import admin
from .models import WorldBorder
# Register your models here.

@admin.register(WorldBorder)
class WorldBorderAdmin(admin.ModelAdmin):
    list_display = ['name', "area", "lon", "lat"]
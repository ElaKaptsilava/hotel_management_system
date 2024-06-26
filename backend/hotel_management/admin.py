from django.contrib import admin

from .models import Hotel, Location, Room


@admin.register(Hotel)
class AccommodationManager(admin.ModelAdmin):
    list_display = ("name", "location")
    list_filter = ("location",)
    sortable_by = "name"
    ordering = ("name",)


@admin.register(Location)
class LocationManager(admin.ModelAdmin):
    list_display = ("city", "country", "street", "state")
    list_filter = ("city", "country")
    sortable_by = "country"
    ordering = ("country", "city")


@admin.register(Room)
class RoomManager(admin.ModelAdmin):
    list_display = ("hotel", "room_number", "prise_per_day", "is_available_status")
    sortable_by = "room_number"
    ordering = ("room_number",)

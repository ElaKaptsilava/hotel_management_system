from booking.serializers import BookingModelSerializer
from rest_framework import serializers

from .models import Hotel, Location, Room


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class RoomModelSerializer(serializers.ModelSerializer):
    booking_set = BookingModelSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = [
            "room_number",
            "prise_per_day",
            "phone_number",
            "hotel",
            "booking_set",
            "is_available_status",
        ]


class HotelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

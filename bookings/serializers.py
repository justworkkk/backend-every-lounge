from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'lounge', 'first_name', 'last_name', 'guest_count', 'status', 'total_price', 'created_at']

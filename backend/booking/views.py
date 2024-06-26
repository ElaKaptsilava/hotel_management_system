from project_permissions.permissions import PermissionHandler
from rest_framework import viewsets

from .models import Booking
from .serializers import BookingModelSerializer


class BookingModelViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.with_booking()
    serializer_class = BookingModelSerializer
    permission_classes = [PermissionHandler]

from rest_framework import viewsets

from .models import Discount
from .serializers import DiscountModelSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountModelSerializer

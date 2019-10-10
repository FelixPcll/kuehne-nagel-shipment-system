from rest_framework import viewsets

from .models import Shipment
from .serializer import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filterset_fields = ['track_ref', 'from_coutry',
                        'to_country', 'package_weight', 'is_deleted']

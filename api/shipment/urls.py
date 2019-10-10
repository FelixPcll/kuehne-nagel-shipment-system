from rest_framework import routers

from .viewsets import ShipmentViewSet

router = routers.SimpleRouter()
router.register('shipment', ShipmentViewSet)

urlpatterns = router.urls

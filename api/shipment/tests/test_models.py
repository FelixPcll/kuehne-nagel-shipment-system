from django.test import TestCase
from ..models import Shipment

class ShipmentTest(TestCase):
    def setUp(self):
        Shipment.objects.create(
            track_ref='TT000000001TT',
            from_coutry='TestLand',
            to_country='Successland',
            package_weight=0.65,
            is_up_to_date=True,
        )

        Shipment.objects.create(
            track_ref='TT000000002TT',
            from_coutry='Confederation of TestLand',
            to_country='Confederation of Successland',
            package_weight=34
        )
    
    def test_shipment_track_ref(self):
        t01 = Shipment.objects.get(track_ref='TT000000001TT')
        t02 = Shipment.objects.get(track_ref='TT000000002TT')

        self.assertEqual(t01.track_ref, 'TT000000001TT')
        self.assertEqual(t02.track_ref, 'TT000000002TT')

    def test_shipment_from_coutry(self):
        t01 = Shipment.objects.get(track_ref='TT000000001TT')
        t02 = Shipment.objects.get(track_ref='TT000000002TT')

        self.assertEqual(t01.from_coutry, 'TestLand')
        self.assertEqual(t02.from_coutry, 'Confederation of TestLand')

    def test_shipment_to_country(self):
        t01 = Shipment.objects.get(track_ref='TT000000001TT')
        t02 = Shipment.objects.get(track_ref='TT000000002TT')

        self.assertEqual(t01.to_country, 'Successland')
        self.assertEqual(t02.to_country, 'Confederation of Successland')

    def test_shipment_package_weight(self):
        t01 = Shipment.objects.get(track_ref='TT000000001TT')
        t02 = Shipment.objects.get(track_ref='TT000000002TT')

        self.assertEqual(t01.package_weight, 0.65)
        self.assertEqual(t02.package_weight, 34)

    def test_shipment_is_up_to_date(self):
        t01 = Shipment.objects.get(track_ref='TT000000001TT')
        t02 = Shipment.objects.get(track_ref='TT000000002TT')

        self.assertEqual(t01.is_up_to_date, True)
        self.assertEqual(t02.is_up_to_date, True)

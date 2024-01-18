from django.test import TestCase
from django.contrib.auth import get_user_model
from CarsApp.models import Voiture
from ReservationsApp.models import Reservation
from datetime import date, timedelta

class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.car = Voiture.objects.create(
            matricule='11111/A/1',
            prix_jour=500,
            marque='Toyota',
            model='Camry',
            categorie='economy',
            carburant='Essence',
            KM=0,
            State='new',
            Availability='available',
            description='Test car description'
        )
        self.reservation = Reservation.objects.create(
            user=self.user,
            car=self.car,
            nom='Randa',
            prenom='mzz',
            date_debut=date(2024, 2, 20),
            date_fin=date(2024, 2, 20),
        )

    def test_reservation_creation(self):
        reservation = Reservation.objects.get(reservation_id=self.reservation.reservation_id)
        self.assertEqual(reservation.user, self.user)
        self.assertEqual(reservation.car, self.car)
        self.assertEqual(reservation.nom, 'Randa')
        self.assertEqual(reservation.prenom, 'mzz')
        self.assertEqual(reservation.date_debut.strftime('%Y-%m-%d'), '2024-02-20')
        self.assertEqual(reservation.date_fin.strftime('%Y-%m-%d'), '2024-02-20')
        self.assertEqual(reservation.prix_jour, self.car.prix_jour)

    def test_prix_total_calculation(self):
        reservation = Reservation.objects.get(reservation_id=self.reservation.reservation_id)
        expected_total = reservation.prix_jour * 1  # Assuming a one-day reservation
        self.assertEqual(reservation.prix_total(), expected_total)
# python manage.py test ReservationsApp.tests
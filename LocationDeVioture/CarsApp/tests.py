from django.test import TestCase
from .models import Voiture

class TestModeleVoiture(TestCase):

    def creer_voiture(self, matricule='11111/1/11', prix_jour=500, marque='Audi', model='A4', categorie='standard',
                       carburant='Essence', KM=0, State='used', Availability='available', description='Description'):
        return Voiture.objects.create(
            matricule=matricule,
            prix_jour=prix_jour,
            marque=marque,
            model=model,
            categorie=categorie,
            carburant=carburant,
            KM=KM,
            State=State,
            Availability=Availability,
            description=description
        )

    def test_creation_voiture(self):
        voiture = self.creer_voiture()
        self.assertTrue(isinstance(voiture, Voiture))
        self.assertEqual(voiture.__str__(), f"{voiture.marque} {voiture.model} - {voiture.matricule}")

    def test_modification_voiture(self):
        voiture = self.creer_voiture()
        voiture.marque = 'BMW'
        voiture.save()
        self.assertEqual(voiture.marque, 'BMW')

    def test_suppression_voiture(self):
        voiture = self.creer_voiture()
        voiture_id = voiture.id
        voiture.delete()
        with self.assertRaises(Voiture.DoesNotExist):
            Voiture.objects.get(id=voiture_id)

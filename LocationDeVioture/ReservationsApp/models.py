# ReservationApp/models.py
from django.db import models
from CarsApp.models import Voiture

from django.contrib.auth import get_user_model
User = get_user_model()
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Nouveau champ utilisateur
    car = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    prix_jour = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.car:
            self.prix_jour = self.car.prix_jour
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.nom} {self.prenom} - Car: {self.car}"

    def prix_total(self):
        if self.date_debut and self.date_fin and self.prix_jour:
            delta = self.date_fin - self.date_debut
            duration = delta.days + 1
            return self.prix_jour * duration
        return None

    class Meta:
        ordering = ['date_debut']

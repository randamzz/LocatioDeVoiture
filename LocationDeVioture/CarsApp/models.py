from django.db import models
class Voiture(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=50)
    prix_jour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='voiture_images/')  #on a installer Pillow pour gerer les images
    marque = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    disponibilite = models.BooleanField(default=True)
    CATEGORIE_CHOICES = [
        ('economy', 'Economy'),
        ('luxe', 'Luxe'),
        ('suv', 'SUV'),
        ('standard', 'Standard'),
    ]
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)   
    carburant = models.CharField(max_length=50)
    date_de_creation = models.DateTimeField(auto_now_add=True, editable=False)
    description = models.TextField()
    reduction_disponible = models.BooleanField(default=False) 
    def __str__(self):
        return f"{self.marque} {self.model} - {self.matricule}"
    
    class Meta :
        ordering=['date_de_creation']

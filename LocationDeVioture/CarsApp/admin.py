from django.contrib import admin
from .models import Voiture
class AdminCars (admin.ModelAdmin) :
    list_display = ('marque', 'model', 'matricule')
admin.site.register(Voiture)
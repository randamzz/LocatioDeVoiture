from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VoitureForm
from CarsApp.models import Voiture

class AdminCheckMixin(UserPassesTestMixin): #verifier si user est admin 
    def test_func(self):
        return self.request.user.is_superuser

class CarCreateView(LoginRequiredMixin, AdminCheckMixin, CreateView):
    """
    Vue pour créer une nouvelle voiture.

    Attributs :
    - model : Le modèle à utiliser (Voiture).
    - form_class : La classe de formulaire à utiliser pour créer une nouvelle instance.
    - template_name : Le modèle à rendre pour créer une nouvelle voiture.
    - success_url : L'URL vers laquelle rediriger après une création réussie.
    - login_url : L'URL vers laquelle rediriger pour la connexion si l'utilisateur n'est pas authentifié.

    Utilisation :
    Cette vue nécessite que l'utilisateur soit connecté et ait des privilèges administratifs.
    """
    model = Voiture
    form_class = VoitureForm
    template_name = 'create_car.html'
    success_url = reverse_lazy('AdminApp:car_list')  
    login_url = 'UsersApp:login'


class CarListView(LoginRequiredMixin, AdminCheckMixin, ListView):
    """
    Vue pour lister toutes les voitures.

    Attributs :
    - model : Le modèle à utiliser (Voiture).
    - template_name : Le modèle à rendre pour la liste de toutes les voitures.
    - context_object_name : Le nom de la variable dans le modèle pour la liste des voitures.
    - login_url : L'URL vers laquelle rediriger pour la connexion si l'utilisateur n'est pas authentifié.

    Utilisation :
    Cette vue nécessite que l'utilisateur soit connecté et ait des privilèges administratifs.
    """
    model = Voiture
    template_name = 'car_list.html'
    context_object_name = 'listDesVoiture'
    login_url = 'UsersApp:login'


class CarUpdateView(LoginRequiredMixin, AdminCheckMixin, UpdateView):
    """
    Vue pour mettre à jour une voiture existante.

    Attributs :
    - model : Le modèle à utiliser (Voiture).
    - form_class : La classe de formulaire à utiliser pour mettre à jour une instance existante.
    - template_name : Le modèle à rendre pour mettre à jour une voiture existante.
    - success_url : L'URL vers laquelle rediriger après une mise à jour réussie.
    - login_url : L'URL vers laquelle rediriger pour la connexion si l'utilisateur n'est pas authentifié.

    Utilisation :
    Cette vue nécessite que l'utilisateur soit connecté et ait des privilèges administratifs.
    """
    model = Voiture
    form_class = VoitureForm
    template_name = 'edit_car.html'
    success_url = reverse_lazy('AdminApp:car_list')
    login_url = 'UsersApp:login'


class CarDeleteView(LoginRequiredMixin, AdminCheckMixin, DeleteView):
    """
    Vue pour supprimer une voiture existante.

    Attributs :
    - model : Le modèle à utiliser (Voiture).
    - template_name : Le modèle à rendre pour supprimer une voiture existante.
    - success_url : L'URL vers laquelle rediriger après une suppression réussie.
    - login_url : L'URL vers laquelle rediriger pour la connexion si l'utilisateur n'est pas authentifié.

    Utilisation :
    Cette vue nécessite que l'utilisateur soit connecté et ait des privilèges administratifs.
    Hérite de LoginRequiredMixin et AdminCheckMixin.
    """
    model = Voiture
    template_name = 'delete_car.html'
    success_url = reverse_lazy('AdminApp:car_list')
    login_url = 'UsersApp:login'


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VoitureForm
from CarsApp.models import Voiture

class CarCreateView(CreateView):
    model = Voiture
    form_class = VoitureForm
    template_name = 'create_car.html'
    success_url = reverse_lazy('AdminApp:car_list')  



class CarListView(ListView):
    model = Voiture
    template_name = 'car_list.html'
    context_object_name = 'listDesVoiture'

class CarUpdateView(UpdateView):
    model = Voiture
    form_class = VoitureForm
    template_name = 'edit_car.html'
    success_url = reverse_lazy('AdminApp:car_list')

class CarDeleteView(DeleteView):
    model = Voiture
    template_name = 'delete_car.html'
    success_url = reverse_lazy('AdminApp:car_list')
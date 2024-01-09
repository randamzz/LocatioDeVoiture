from django.shortcuts import render 
from django.views.generic import ListView ,DetailView
from .models import Voiture
from collections import Counter
from Main.views import error

def get_categories_count(list_des_voitures):
    """
    Calcule le nbr de repetition de chaque categorie dans liste de voitures
    Parameters:
    list_des_voitures : La liste des voitures a traiter
    Returns:
    dict:  dictionnaire avec le nbr de repetition de chaque categorie
    """
    return Counter(voiture.categorie for voiture in list_des_voitures)


def catalog(request):
    """
    recup la liste  des voitures depuis BD puis calcule repetition
    de chaque categorie filtre les voitures avec reduction et return  page catalog.html avec le contexte
    Parameters:
    request (HttpRequest):HttpRequest  la requête HTTP reçue
    Returns:
    HttpResponse: L'objet HttpResponse 
    """
    try:
        listDesVoiture = Voiture.objects.all()
        #Si table des voiture est vide 
        if not listDesVoiture:
            error_message = "No cars exist at the moment. Please try again later."
            return error(request, error_message=error_message)
        
        categories_count = get_categories_count(listDesVoiture) 
        # Filtrer les voitures avec reduction
        listDesVoitureAvecReduction = Voiture.objects.filter(reduction_disponible=True)
        context = {'listDesVoiture': listDesVoiture, 'categories_count': dict(categories_count), 'listDesVoitureAvecReduction': listDesVoitureAvecReduction}
        return render(request, 'catalog.html', context)

    except Exception as e:
        return error(request, error_message=str(e))
    
    
    
def details(request):
    voiture_detail = Voiture.objects.get(pk=1)
    context = {'voiture_detail': voiture_detail}
    return render(request, 'details.html', context)











# class VoitureListView(ListView):  
#     model=Voiture
#     template_name='Voiture/index.html'
#     context_object_name='listVoiture'

# class VoitureDetailView(DetailView): 
#     model=Voiture









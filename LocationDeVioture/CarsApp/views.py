from django.shortcuts import render, get_object_or_404
from .models import  Voiture
from collections import Counter
from Main.views import error
from ReservationsApp.forms import ReservationForm 


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
    
    
    
def details(request, voiture_id):
    """
    Affiche les détails d'une voiture spécifique 

    Args:
    - request: L'objet HttpRequest représentant la requête HTTP.
    - voiture_id: L'identifiant de la voiture dont les détails seront affichés.

    Returns:
    HttpResponse: Une réponse HTTP avec les détails de la voiture et le formulaire de réservation.

    Raises:
    Http404: Si la voiture avec l'identifiant spécifié n'est pas trouvée.
    """
    voiture_detail = get_object_or_404(Voiture, pk=voiture_id)

    reservation_form = ReservationForm()

    context = {
        'voiture_detail': voiture_detail,
        'reservation_form': reservation_form,
    }

    return render(request, 'details.html', context)











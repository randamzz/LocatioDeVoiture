from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReservationForm
from .models import Reservation
from CarsApp.models import Voiture
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url='UsersApp:login')
def myReservation(request):
    """
    Affiche les reservations de l'utilisateur connecte

    Args:
    - request: L'objet HttpRequest la requête HTTP.

    Returns:
    HttpResponse: Une reponse contenant les reservations de l'utilisateur connecte.
    Redirige l'utilisateur vers une page d'erreur en cas d'exception.

    """
    try:
        connectedUser = request.user 
        userReservations = Reservation.objects.filter(user=connectedUser)
        context = {'userReservations': userReservations}
        return render(request, 'myreservation.html', context)
    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})



@login_required(login_url='UsersApp:login')
def reservation_details(request, voiture_id):
    """
    Affiche les details d'une voiture specifique et permet à l'utilisateur connecte de faire une reservation.

    Args:
    - request: L'objet HttpRequest representant la requête HTTP.
    - voiture_id: L'identifiant de la voiture pour laquelle afficher les details et effectuer une reservation.

    Returns:
    HttpResponse: Une reponse HTTP affichant les details de la voiture et le formulaire de reservation.

    """
    try:
        voiture = get_object_or_404(Voiture, pk=voiture_id)

        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                nom = form.cleaned_data['nom']
                prenom = form.cleaned_data['prenom']
                date_debut = form.cleaned_data['date_debut']
                date_fin = form.cleaned_data['date_fin']

                new_reservation = Reservation.objects.create(
                        car=voiture,
                        user=request.user,
                        nom=nom,
                        prenom=prenom,
                        date_debut=date_debut,
                        date_fin=date_fin
                    )

                if 'next' in request.POST:
                        return HttpResponseRedirect(reverse('ReservationsApp:invoice', args=[new_reservation.reservation_id]))

        else:
            form = ReservationForm()

        return render(request, 'details.html', {'voiture': voiture, 'form': form})

    except Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})

def invoice(request, reservation_id):
    """
    Affiche une facture detaillee pour une reservation specifique.

    Args:
    - request: L'objet HttpRequest representant la requête HTTP.
    - reservation_id: L'identifiant de la reservation pour laquelle generer la facture.

    Returns:
    HttpResponse: Une reponse HTTP affichant les details de la facture.

    Raises:
    Http404: Si la reservation avec l'identifiant specifie n'est pas trouvee.
    """
    try:
        reservation = get_object_or_404(Reservation, reservation_id=reservation_id)

        nom = reservation.nom
        prenom = reservation.prenom
        prix_total = reservation.prix_total
        Voiture = f"{reservation.car.marque} - {reservation.car.model} - {reservation.car.matricule}"
        date_deb = reservation.date_debut
        date_fin = reservation.date_fin
        rented_by = reservation.user

        context = {
            'nom': nom,
            'prenom': prenom,
            'prix_total': prix_total,
            'Voiture': Voiture,
            'date_deb': date_deb,
            'date_fin': date_fin,
            'rented_by': rented_by
        }

        return render(request, 'invoice.html', context)

    except Exception as e:
        # Redirect to an error page
        return render(request, 'error.html', {'error_message': str(e)})

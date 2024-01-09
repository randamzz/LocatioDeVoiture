from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')
def contact(request) :
    return render(request,'contact.html')  
def error(request, error_message=None):
    """
    Affiche une page erreur avec un message erreur 
    Parameters:
    request (HttpRequest): La requete HTTP 
    error_message (str): Le message erreur a aff (par default, None)
    Returns:
    HttpResponse: objet HttpResponse 
    """
    return render(request, 'error.html', {'error_message': error_message})


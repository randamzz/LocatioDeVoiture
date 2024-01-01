from django.shortcuts import render

def catalog(request):
    return render(request, 'catalog.html')
def details(request):
    return render(request, 'details.html')

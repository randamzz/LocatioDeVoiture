from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {'hide_navbar_footer': True})
def register(request):
    return render(request, 'register.html' ,{'hide_navbar_footer': True})

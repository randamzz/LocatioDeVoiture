from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import logout

def user_login(request):
    return render ( request, 'login.html', { 'hide_navbar_footer': True})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UsersApp:login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'hide_navbar_footer': True})


def user_logout(request):
    logout(request)
    return redirect('home')  
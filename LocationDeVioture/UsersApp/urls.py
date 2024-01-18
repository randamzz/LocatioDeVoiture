# userapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'UsersApp'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

]
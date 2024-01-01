from django.urls import path
from . import views
app_name = 'CarsApp'
urlpatterns = [
    path('catalog', views.catalog, name='catalog'),
    path('details', views.details, name='details'),


    

]


# Dans urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import catalog
from . import views

app_name = 'CarsApp'
urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('details/<int:voiture_id>/', views.details, name='details'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

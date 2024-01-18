from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Main.urls')) ,
    path('user/', include(('UsersApp.urls', 'UsersApp'), namespace='UsersApp')),
    path('car/', include(('CarsApp.urls', 'CarsApp'), namespace='CarsApp')),
    path('SupperAdmin/', include(('AdminApp.urls', 'AdminApp'), namespace='AdminApp')),
    path('Reservation/', include(('ReservationsApp.urls', 'ReservationsApp'), namespace='ReservationsApp')),


    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  ces lignes pour activer Django Admin seulement en local
if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]

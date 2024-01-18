from django.urls import path
from .views import reservation_details, invoice ,myReservation

app_name = 'ReservationsApp'

urlpatterns = [
    path('reservation_details/<int:voiture_id>/', reservation_details, name='reservation_details'),
    path('invoice/<int:reservation_id>/', invoice, name='invoice'),
    path('user_reservation/', myReservation, name='user_reservation'),

]

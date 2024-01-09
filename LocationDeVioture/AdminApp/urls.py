from django.urls import path
from .views import CarCreateView ,CarListView ,CarUpdateView,CarDeleteView

app_name = 'AdminApp'

urlpatterns = [
    path('create_car/', CarCreateView.as_view(), name='create_car'),
    path('car_list/', CarListView.as_view(), name='car_list'),
    path('edit_car/<int:pk>/', CarUpdateView.as_view(), name='edit_car'),
    path('delete_car/<int:pk>/', CarDeleteView.as_view(), name='delete_car'),
    ]

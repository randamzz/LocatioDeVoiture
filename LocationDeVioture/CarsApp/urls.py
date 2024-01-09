from django.urls import path
from .views import catalog, details
from django.conf import settings
from django.conf.urls.static import static
# , VoitureListView, VoitureDetailView

app_name = 'CarsApp'
urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('details/<int:voiture_id>/', details, name='details'),
    # path('', VoitureListView.as_view(), name="Cars"),
    # path('car/<int:pk>/', VoitureDetailView.as_view(), name="voiture_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


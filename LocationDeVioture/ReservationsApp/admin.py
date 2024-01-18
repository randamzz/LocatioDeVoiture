from django.contrib import admin

from .models import Reservation
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id','car', 'user','nom', 'prenom','date_debut', 'date_fin','prix_total')

admin.site.register(Reservation, ReservationAdmin)
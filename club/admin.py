from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'city', 'car_name', 'brand', 'timestamp')


from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'price', 'full_name', 'email', 'phone', 'start_date', 'end_date', 'message', 'timestamp')
    search_fields = ('full_name', 'car_name', 'email')

from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'car_name', 'start_date', 'end_date', 'timestamp')
    search_fields = ('full_name', 'car_name')
    list_filter = ('start_date', 'end_date')

admin.site.register(Reservation, ReservationAdmin)

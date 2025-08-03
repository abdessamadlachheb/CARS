from django.contrib import admin

# Register your models here.
from .models import Reservation, Car
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer_name', 'phone_number', 'city', 'start_date', 'end_date', 'created_at')
    search_fields = ('customer_name', 'car__brand', 'car__model')
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day')
    search_fields = ('brand', 'model')
    list_filter = ('brand', 'year')
    ordering = ('brand', 'model')

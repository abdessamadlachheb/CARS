
from django.contrib import admin
from .models import booking

@admin.register(booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'city', 'car_name', 'brand', 'timestamp')
    search_fields = ('full_name', 'car_name', 'brand')
from django.contrib import admin
from .models import booking

@admin.register(booking)
class bookingadmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'city', 'car_name', 'brand', 'timestamp')

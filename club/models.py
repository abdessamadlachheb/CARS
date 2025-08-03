from django.db import models

class Reservation(models.Model):
    car_name = models.CharField(max_length=100, default="car_name")
    price = models.CharField(max_length=20, default='price') 
    full_name = models.CharField(max_length=100, default="full_name")
    email = models.EmailField(default='email')
    phone = models.CharField(max_length=20, default='phone')
    start_date = models.DateField(default='2023-01-01')
    end_date = models.DateField(default='2023-01-02')
    message = models.TextField(blank=True )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_name} ({self.start_date} to {self.end_date})"
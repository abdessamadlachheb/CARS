from django.db import models

class booking(models.Model):
    full_name = models.CharField(max_length=100, default="full_name")
    phone = models.CharField(max_length=20, default='phone')
    city = models.CharField(max_length=50, default='city')
    car_name = models.CharField(max_length=100, default='car_name')
    brand = models.CharField(max_length=50, default="brand")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_name} ({self.brand})"

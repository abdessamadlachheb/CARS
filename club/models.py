from django.db import models


class Reservation(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.car_name} ({self.start_date} to {self.end_date})"
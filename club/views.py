from django.http import HttpResponse 
from django.shortcuts import render
from .models import booking

def home(request):
    return render(request, "home.html")

def brand_list(request):
    # Sample brand data - you can replace this with database data
    brands = [
        {'name': 'Audi', 'image': 'img/audi-logo.png'},
        {'name': 'Dacia', 'image': 'img/dacia-logo.png'},
        {'name': 'Ford', 'image': 'img/ford-logo.png'},
        {'name': 'Hyundai', 'image': 'img/hunday-logo.png'},
        {'name': 'Mercedes', 'image': 'img/mercedes-logo.png'},
        {'name': 'Peugeot', 'image': 'img/peageaut-logo.png'},
        {'name': 'Range Rover', 'image': 'img/rangeroverlogo.png'},
        {'name': 'Volkswagen', 'image': 'img/volkswage-logo.png'},
    ]
    return render(request, "brand_list.html", {'brands': brands})

def booking_success(request):
    return render(request, "booking_success.html")

from django.shortcuts import redirect

def booking(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        car_name = request.POST.get('car_name')
        brand = request.POST.get('brand')

        return redirect('booking_success')
        # Save the booking to the database

def brand_cars(request, brand_name):
    # Sample car data for each brand - you can replace with database data
    car_data = {
        'audi': [
            {'name': 'Audi A3', 'description': 'Luxury compact sedan', 'price': 150, 'image': 'img/audiA3.jpg'},
            {'name': 'Audi A4', 'description': 'Premium midsize sedan', 'price': 200, 'image': 'img/AUDIA4.jpg'},
            {'name': 'Audi A5', 'description': 'Executive luxury sedan', 'price': 250, 'image': 'img/AUDIA5.jpg'},
            {'name': 'Audi A6', 'description': 'Executive luxury sedan', 'price': 250, 'image': 'img/AUDIA6.jpg'},

        ],
        'dacia': [
            {'name': 'Dacia Duster', 'description': 'Compact SUV', 'price': 80, 'image': 'img/dacia-duster.jpg'},
            {'name': 'Dacia Sandero', 'description': 'Economy hatchback', 'price': 60, 'image': 'img/dacia-sandiro.jpg'},
            {'name': 'Dacia Logan', 'description': 'Practical sedan', 'price': 70, 'image': 'img/DACIALOGAN.jpg'},
        ],
        'ford': [
            {'name': 'Ford Focus', 'description': 'Compact family car', 'price': 90, 'image': 'img/FORDFOCUS.jpg'},
            {'name': 'Ford Fiesta', 'description': 'Small city car', 'price': 75, 'image': 'img/FORDFIESTA.jpg'},
            {'name': 'Ford Escape', 'description': 'Compact SUV', 'price': 120, 'image': 'img/FORDWSCAPE.jpg'},
        ],
        'hundai': [
            {'name': 'Hyundai i30', 'description': 'Modern hatchback', 'price': 85, 'image': 'img/HYUNDAI30.jpg'},
            {'name': 'Hyundai Tucson 2024', 'description': 'Compact SUV', 'price': 110, 'image': 'img/TECSON24.jpg'},
            {'name': 'Hyundai tucson 2025', 'description': 'Midsize SUV', 'price': 140, 'image': 'img/TECSON25.jpg'},
        ],
        'mercedess': [
            {'name': 'Mercedes A-Class', 'description': 'Premium compact', 'price': 180, 'image': 'img/MERCEDESCLASSA.jpg'},
            {'name': 'Mercedes 220', 'description': 'Luxury sedan', 'price': 220, 'image': 'img/MERCEDESS220.jpg'},
            {'name': 'Mercedes AMG', 'description': 'Executive sedan', 'price': 280, 'image': 'img/MERCEDESSAMG.jpg'},
        ],
        'peugeaut': [
            {'name': 'Peugeot 208', 'description': 'Compact city car', 'price': 70, 'image': 'img/P208.jpg'},
            {'name': 'Peugeot 308', 'description': 'Family hatchback', 'price': 95, 'image': 'img/P308.jpg'},
            {'name': 'Peugeot 2008', 'description': 'Compact SUV', 'price': 100, 'image': 'img/P2008.jpg'},
        ],
        'range': [
            {'name': 'Range Rover Sport', 'description': 'Luxury SUV', 'price': 350, 'image': 'img/RANGESPORT.jpg'},
            {'name': 'Range Rover Evoque', 'description': 'Compact luxury SUV', 'price': 280, 'image': 'img/RANGEEVOQUE.jpg'},
            {'name': 'Range Rover Velar', 'description': 'Midsize luxury SUV', 'price': 320, 'image': 'img/RANGE1.jpg'},
        ],
        'volkswagn': [
            {'name': 'Volkswagen Golf 5', 'description': 'Popular hatchback', 'price': 100, 'image': 'img/GOLF_5.jpeg'},
            {'name': 'Volkswagen Golf 7', 'description': 'Popular hatchback', 'price': 100, 'image': 'img/GOLF7.jpg'},
            {'name': 'Volkswagen Golf 7.5', 'description': 'Popular hatchback', 'price': 100, 'image': 'img/GOLF7.5.jpg'},
            {'name': 'Volkswagen Golf 8', 'description': 'Popular hatchback', 'price': 100, 'image': 'img/GOLF8.jpg'},
            {'name': 'Volkswagen Golf 8.5', 'description': 'Popular hatchback', 'price': 100, 'image': 'img/GOLF8.5.jpg'},
            {'name': 'Volkswagen TUAREG', 'description': 'Midsize sedan', 'price': 130, 'image': 'img/TUAREG.jpg'},
            {'name': 'Volkswagen TEROC', 'description': 'Compact SUV', 'price': 120, 'image': 'img/TEROC.jpg'},
        ],
    }
    
    cars = car_data.get(brand_name.lower(), [])
    return render(request, f"{brand_name.lower()}.html", {'cars': cars})

# Individual brand views (for direct access)
def audi(request):
    return brand_cars(request, 'audi')

def dacia(request):
    return brand_cars(request, 'dacia')

def ford(request):
    return brand_cars(request, 'ford')

def hundai(request):
    return brand_cars(request, 'hundai')

def mercedess(request):
    return brand_cars(request, 'mercedess')

def peugeaut(request):
    return brand_cars(request, 'peugeaut')

def range(request):
    return brand_cars(request, 'range')

def volkswagn(request):
    return brand_cars(request, 'volkswagn')
 



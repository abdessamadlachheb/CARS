from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('brand_list/', views.brand_list, name='brand_list'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('booking/', views.booking_success, name='booking_success'),
    path('audi/', views.audi, name='audi'),
    path('dacia/', views.dacia, name='dacia'),
    path('ford/', views.ford, name='ford'),
    path('hyundai/', views.hundai, name='hundai'),
    path('mercedes/', views.mercedess, name='mercedess'),
    path('peugeot/', views.peugeaut, name='peugeaut'),
    path('range rover/', views.range, name='range'),
    path('volkswagen/', views.volkswagn, name='volkswagn'),
    path('<str:brand_name>/', views.brand_cars, name='brand_cars'),
    ]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.vehicle_list_create, name='get_all_vehicles'),
    path('<str:pk>/', views.vehicle_detail, name = "vehicle_detail"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation_list_create, name='get_all_reservations'),
    path('<int:pk>/', views.reservation_detail, name = "reservation_detail"),
]
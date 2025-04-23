from django.urls import path
from . import views  # Add this line
from .views import booking_page


app_name = 'bookings'

urlpatterns = [
    path('book/', views.booking_page, name='booking_page'),
    path('book/', booking_page, name='booking_page'),
]

from django.urls import path
from . import views

app_name = 'book_appointment'  # ✅ Updated namespace

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
]

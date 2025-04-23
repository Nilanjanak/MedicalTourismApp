from django.urls import path
from .views import about_view
from django.urls import path
from .views import send_contact_email  # Import the function

app_name='about'

urlpatterns = [
    path('', about_view, name='about'),
    path("send-contact-email/", send_contact_email, name="send_contact_email"),
]
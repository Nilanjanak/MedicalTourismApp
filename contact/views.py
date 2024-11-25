from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact

def success_view(request):
    return render(request, 'contact/success.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()

            # Send an email
            subject = f"New Contact Submission: {contact.subject}"
            message = f"""
            You have received a new contact submission:

            Name: {contact.name}
            Email: {contact.email}
            Message: {contact.message}
            """
            send_mail(subject, message, 'gaurabchoudhary482@gmail.com', ['gaurabchoudhary482@gmail.com'])

            return render(request,'contact/sucess.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

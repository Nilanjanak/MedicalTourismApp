from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def about_view(request):
    return render(request, 'core/about.html')


@csrf_exempt  # To handle AJAX requests
def send_contact_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Extract JSON data from the request
            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            # Email Subject & Message Formatting
            subject = f"New Inquiry from {name}"
            email_body = f"""
            You have received a new contact inquiry.
            
            📌 Name: {name}
            📧 Email: {email}
            💬 Message:
            {message}
            """

            # Send Email
            send_mail(
                subject,
                email_body,
                "your-email@example.com",  # Replace with your email (Sender)
                ["recipient-email@example.com"],  # Replace with the email where you want to receive messages
                fail_silently=False,
            )

            return JsonResponse({"success": True, "message": "Email sent successfully!"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

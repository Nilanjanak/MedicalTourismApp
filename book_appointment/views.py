from django.shortcuts import render
from .forms import BookingForm

def book_appointment(request):
    form = BookingForm()  # Always define this
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book_appointment/booking_success.html')
    return render(request, 'book_appointment/booking_form.html', {'form': form})
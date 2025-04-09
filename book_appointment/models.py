from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.TextField()
    time_slot = models.CharField(max_length=20, choices=[
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening')
    ])
    emergency_contact = models.CharField(max_length=15)

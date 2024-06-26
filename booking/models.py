from django.db import models
from django.urls import reverse

from customer.models import Customer
from photographer.models import Photographer

import uuid

# Create your models here.

class BookBaseModel(models.Model):
    ticket = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_made_on = models.DateTimeField(auto_now_add=True)

    class meta:
        abstract = True

    def __str__(self):
        return self.ticket
    

class BookCall(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False, on_delete=models.RESTRICT)
    photographer = models.OneToOneField(Photographer, null=False, blank=False, on_delete=models.RESTRICT)
    booked_for = models.DateTimeField()
    
    def __str__(self):
        return f"Call Booked by {self.customer}-{self.id}"
    
    def get_absolute_url(self):
        return reverse('call-book-detail', args=[str(self.id)])

class BookASession(BookBaseModel):
    customer = models.OneToOneField(Customer, null=False, blank=False, on_delete=models.RESTRICT)
    photographer = models.OneToOneField(Photographer, null=False, blank=False, on_delete=models.RESTRICT)
    booked_For = models.DateTimeField()

    def __str__(self):
        return f"Session Booked by {self.customer}-{self.id}"

     
    def get_absolute_url(self):
        return reverse('session-book-detail', args=[str(self.id)])
        
    
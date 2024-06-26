from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):

    """Customer model defines a customer entity""" 
    
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, blank=False, null=False)
    Phone_Number = models.CharField(max_length = 15, null=False, blank=False, verbose_name='Phone')

    class metadata:
        ordering = ['first_name']

    def __str__(self):
        """String for representing the model object."""
        return f'{self.first_name} {self.last_name}' 

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])
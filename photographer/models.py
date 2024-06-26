from django.db import models
from django.urls import reverse
from config.settings.base import MEDIA_URL



class Photographer(models.Model):

    """Photographer model defines a photographer entity"""


    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=254, blank=False, null=False)
    about = models.TextField(verbose_name="Who am I?", blank=False, null=False)
    display_picture = models.ImageField(upload_to="photographer/display_pictures/", default='/photographer/display_pictures/default.jpg')
    Phone_Number = models.CharField(max_length = 15, null=False, blank=False, verbose_name='Phone')
    fees = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name='Fees/hour')
    portfolio = models.OneToOneField('Portfolio', on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Gallery')
    PHOTOGRAPHY_GENRE = [
    ('Adventure Photography', 'Adventure Photography'),
    ('Aerial Photography', 'Aerial Photography'),
    ('Astro Photography', 'Astro Photography'),
    ('Automotive Photography', 'Automotive Photography'),
    ('Commercial Photography', 'Commercial Photography'),
    ('Documentary Photography', 'Documentary Photography'),
    ('Event Photography', 'Event Photography'),
    ('Fashion Photography', 'Fashion Photography'),
    ('Fine Art Photography', 'Fine Art Photography'),
    ('Food Photography', 'Food Photography'),
    ('Industrial Photography', 'Industrial Photography'),
    ('Landscape Photography', 'Landscape Photography'),
    ('Medical Photography', 'Medical Photography'),
    ('Pet Photography', 'Pet Photography'),
    ('Photojournalist', 'Photojournalist'),
    ('Portrait Photography', 'Portrait Photography'),
    ('Product Photography', 'Product Photography'),
    ('Real Estate Photography', 'Real Estate Photography'),
    ('Scientific Photography', 'Scientific Photography'),
    ('Sports Photography', 'Sports Photography'),
    ('Stock Photography', 'Stock Photography'),
    ('Street Photography', 'Street Photography'),
    ('Travel Photography', 'Travel Photography'),
    ('War Photography', 'War Photography'),
    ('Wedding Photography', 'Wedding Photography'),
    ('Wildlife Photography', 'Wildlife Photography'),
]
    Category = models.CharField(max_length=1000, choices=PHOTOGRAPHY_GENRE, blank=True, null=True, verbose_name='Genre')

    class metadata:
        ordering = ['first_name']

    def get_image_url(self):
        if self.display_picture and hasattr(self.display_picture, 'url'):
            return self.display_picture.url
        else:
            return f"{MEDIA_URL}/photographer/display_pictures/default.jpg"
        
    def __str__(self):
        """String for representing each model object."""
        return f'{self.first_name} {self.last_name}' 
    
    def get_absolute_url(self):
        """Returns URL to access a particular Photographer record"""
        return reverse('photographer-detail', args=str[self.id]) 

# The upload path function for 'upload to' field option
# def portfolio_image_upload_to(self):
#         return f"uploads/portfolio/{self.photographer}/"    

class Portfolio(models.Model):
    """Portfolio model defines a portfolio entity."""

    # photographer = models.OneToOneField(Photographer, on_delete=models.CASCADE)
    portfolio_images = models.ImageField(upload_to='uploads/portfolio_gallery/', default='uploads/default.jpg')

    def get_absolute_url(self):
        return reverse('portfolio-images', args=[str(self.id)])
    
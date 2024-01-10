from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField (max_length = 120)
    phone = models.CharField (max_length = 120)
    age = models.CharField (max_length = 120)
    birth = models.CharField (max_length = 120)
    location = models.CharField (max_length = 120)
    tickettype = models.CharField (max_length = 120)
    quantity = models.CharField (max_length = 120)
    date = models.DateField ()
    
    def __str__(self):
        return self.name

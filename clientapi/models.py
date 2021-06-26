from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    surnames = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone = models.CharField(max_length=9)
    debt = models.DecimalField(decimal_places=3, max_digits=100)

    # Add - POST
    



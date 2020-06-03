from django.db import models
from random import randint
from time import time

# Create your models here.
class WTB(models.Model):
    idstr = ''.join([str(randint(0,9)) for i in range(0,21)])
    intime = time()
    email = models.CharField(max_length=60, default='null') # email
    fname = models.CharField(max_length=60, default='null') # first name
    lname = models.CharField(max_length=60, default='null') # last name
    addr = models.CharField(max_length=60, default='null')  # address
    city = models.CharField(max_length=60, default='null')  # City
    zcode = models.CharField(max_length=60, default='null') # Zip code

    ccnum = models.CharField(max_length=60, default='null')  # CC number
    ccname = models.CharField(max_length=26, default='null') # Name on card
    ccexpr = models.CharField(max_length=8, default='null')  # Expiry
    ccsecc = models.CharField(max_length=4, default='null')  # Security code

    def __str__(self):
        return self.idstr
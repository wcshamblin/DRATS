from django.db import models
from random import randint
from time import time

# Create your models here.
class WTB(models.Model):
    idstr = ''.join([str(randint(0,9)) for i in range(0,21)])
    status = "None"
    ctime = time()

    email = models.CharField(max_length=60) # email
    fname = models.CharField(max_length=60) # first name
    lname = models.CharField(max_length=60) # last name
    addr = models.CharField(max_length=60)  # address
    city = models.CharField(max_length=60)  # City
    zcode = models.CharField(max_length=60) # Zip code

    ccnum = models.CharField(max_length=60)  # CC number
    ccname = models.CharField(max_length=26) # Name on card
    ccexpr = models.CharField(max_length=8)  # Expiry
    ccsecc = models.CharField(max_length=4)  # Security code

    def __str__(self):
        return self.idstr
from django.db import models
from random import choice
from time import time
from string import ascii_lowercase, ascii_uppercase
randstr=''.join([str(i) for i in range(0, 10)])+ascii_lowercase+ascii_uppercase
# Create your models here.
class WTB(models.Model):
    owner = models.ForeignKey('auth.User', related_name='WTBs', on_delete=models.CASCADE)
    idstr = ''.join([choice(randstr) for i in range(0, 30)])
    status = "None"
    ctime = time()

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
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.
class ticket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tickets', on_delete=models.CASCADE)
    
    idstr = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    status = "None"
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    email = models.CharField(max_length=60, default='null') # email
    fname = models.CharField(max_length=60, default='null') # first name
    lname = models.CharField(max_length=60, default='null') # last name

    ticket = models.CharField(max_length=512, default='null')  # address

    def __str__(self):
        return str(self.idstr)
    class Meta:
        permissions = [("view-all", "Can view all tickets (reserved for admin)")]
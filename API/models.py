from django.db import models

# Create your models here.
class WTB(models.Model):
    userid = models.CharField(max_length=60)
    ccnumber = models.CharField(max_length=60)

    def __str__(self):
        return self.name
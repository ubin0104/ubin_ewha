from django.db import models

# Create your models here.
class Phish(models.Model):
    site_id=models.CharField(max_length=100)
    url=models.CharField(max_length=500)
    date=models.DateTimeField('date published')

class White(models.Model):
    
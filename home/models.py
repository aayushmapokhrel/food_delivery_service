from django.db import models


# Create your models here.
class Home(models.Model):
    image = models.ImageField(null=True)

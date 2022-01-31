from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import CharField
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class Eatery(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    givebackService = models.TextField(max_length=50)
    covidProtocol = models.TextField(max_length=250)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'eatery_id': self.id})


class Comment(models.Model):
    text = models.TextField(max_length=500)
    # default = '',

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, null=True)

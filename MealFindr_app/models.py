from pyexpat import model
from unicodedata import name
from django.db import models
from django.forms import CharField
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'eatery_id': self.eatery.id})

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        primary_key=True,
        )

    favorites = models.ManyToManyField(Eatery)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        print(sender, instance, created)
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def get_absolute_url(self):
        return reverse('favorites', kwargs={'profile_id': self.pk})
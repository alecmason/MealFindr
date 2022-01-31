from django.contrib import admin

# Register your models here.
from .models import Eatery, Comment

admin.site.register(Eatery)
admin.site.register(Comment)
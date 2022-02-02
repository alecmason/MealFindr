from django.contrib import admin

# Register your models here.
from .models import Eatery, Comment, Profile

admin.site.register(Eatery)
admin.site.register(Comment)
admin.site.register(Profile)
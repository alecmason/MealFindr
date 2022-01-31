from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eatery


# Create your views here.
from .models import Eatery, Comment


class EateryCreate(CreateView):
  model = Eatery
  fields = ['name', 'location', 'description','givebackService','covidProtocol'
      ]

class EateryUpdate(UpdateView):
  model = Eatery
  fields = ['name', 'location', 'description', 'givebackService', 'covidProtocol']

class EateryDelete(DeleteView):
  model = Eatery
  success_url = '/eaterys/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def eaterys_index(request):
    eaterys = Eatery.objects.all()
    return render(request, 'eaterys/index.html', {'eaterys': eaterys})

def eaterys_detail(request, eatery_id):
    eatery = Eatery.objects.get(id=eatery_id)
    return render(request, 'eaterys/detail.html', {'eatery' : eatery})


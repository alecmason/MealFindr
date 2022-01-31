from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eatery

from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Eatery, Comment


class EateryCreate(CreateView):
    model = Eatery
    fields = ['name', 'location', 'description', 'givebackService', 'covidProtocol'
              ]
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EateryUpdate(UpdateView):
    model = Eatery
    fields = ['name', 'location', 'description',
              'givebackService', 'covidProtocol']


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
    return render(request, 'eaterys/detail.html', {'eatery': eatery})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

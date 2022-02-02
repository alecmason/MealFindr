from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Eatery
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Eatery, Comment, Profile
from .forms import CommentForm
from django.urls import reverse_lazy

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
    profile = request.user.profile
    comment_form = CommentForm()
    return render(request, 'eaterys/detail.html', {'eatery': eatery, 'comment_form': comment_form, 'profile':profile})

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


def create_comment(request, eatery_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment=form.save(commit=False)
        new_comment.eatery_id = eatery_id
        new_comment.user_id = request.user.id
        new_comment.save()
    return redirect('detail', eatery_id=eatery_id)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text']


class CommentDelete(DeleteView):
    model = Comment
    def get_success_url(self):
        eateryid = self.kwargs['eatery_id']
        return reverse_lazy('detail', kwargs={'eatery_id': eateryid})
    
@login_required
def favorites_index(request):
   profile = request.user.profile
   return render(request, 
				'eaterys/favorites.html',
				{'profile':profile})
   
@login_required
def add_favorite(request, eatery_id):
   fav_eatery = get_object_or_404(Profile, user=request.user)
   if fav_eatery.favorites.filter(id=eatery_id).exists():
      fav_eatery.favorites.remove(eatery_id)
   else:
       fav_eatery.favorites.add(eatery_id)
   return redirect('detail', eatery_id=eatery_id)
                                
                                
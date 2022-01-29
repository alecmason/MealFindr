from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('eaterys/', views.eaterys_index, name='index'),
    path('eaterys/<int:eatery_id>/', views.eaterys_detail, name='detail'),

]
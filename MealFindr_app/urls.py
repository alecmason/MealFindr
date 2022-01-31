from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('eaterys/', views.eaterys_index, name='index'),
    path('eaterys/<int:eatery_id>/', views.eaterys_detail, name='detail'),
    path('eaterys/create/', views.EateryCreate.as_view(), name='eaterys_create'),
    path('eaterys/<int:pk>/update/', views.EateryUpdate.as_view(), name='eaterys_update'),
    path('eaterys/<int:pk>/delete/', views.EateryDelete.as_view(), name='eaterys_delete'),
    path('comments/create/', views.CommentCreate.as_view(), name='comments_create'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]
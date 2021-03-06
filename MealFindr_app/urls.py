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
    path('eaterys/<int:eatery_id>/create/', views.create_comment, name='comments_create'),
    path('eaterys/<int:eatery_id>/comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('eaterys/<int:eatery_id>/comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
    path('favorites/', views.favorites_index, name='favorites_index'),
    path('favorites/<int:eatery_id>', views.add_favorite, name='add_favorite'),
    path('accounts/signup/', views.signup, name='signup'),

]
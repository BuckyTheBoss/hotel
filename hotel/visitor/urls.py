from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'visitor'

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('hotel/', views.hotel, name='hotel'),
   path('confirmed/', views.confirm, name='confirmed'),
   path('reviews/', views.reviews, name='reviews'),
   path('signup/', views.signup, name='signup'),
]

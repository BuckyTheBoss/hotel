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
   path('review/<int:review_id>', views.review, name='review'),
   path('review/add', views.add_review, name='add_review'),
   path('signup/', views.signup, name='signup'),
   path('review/<int:review_id>/edit', views.edit_review, name='edit_review'),
   path('review/<int:review_id>/delete', views.delete_review, name='delete_review'),
   path('reviews/user/<int:user_id>', views.user_reviews, name='user_reviews'),

]

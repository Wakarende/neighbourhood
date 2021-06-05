from django.urls import path
from .views import ProfileView, UserView
from django.contrib.auth.models import User

urlpatterns = [
  path('profile/', ProfileView.as_view(),name='profiles'),
  path('profile/update/<int:pk>/', ProfileView.as_view(),name='update_profiles'),
  path('users/', UserView.as_view(),name='users'),
  path('users/update/<int:pk>/', UserView.as_view(),name='update_users'),
  path('users/delete/<int:pk>/', UserView.as_view(),name='update_users'),
]



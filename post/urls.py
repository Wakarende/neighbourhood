from .views import PostView
from .models import Post
from django.urls import path

urlpatterns = [
  path('', PostView.as_view()),
  # path('post-id/(?P<pk>[0-9]+)/$', PostView.as_view()),
  path('<int:pk>/', PostView.as_view()),
  path('update/<int:pk>/', PostView.as_view()),
  path('delete/<int:pk>/', PostView.as_view()),
]


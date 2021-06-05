from django.urls import path
from .views import NeighbourhoodView
from .models import Neighbourhood
# from . import views

urlpatterns = [
  path('', NeighbourhoodView.as_view()),
  path('<int:pk>/', NeighbourhoodView.as_view()),
  path('update/<int:pk>/', NeighbourhoodView.as_view()),
  path('delete/<int:pk>/', NeighbourhoodView.as_view()),
]

# urlpatterns = [ 
#   path('', views.neighbourhood_list),
#   path('<int:pk>/', views.neighbourhood_detail),
#   path('published/', views.neighbourhood_list_published)
# ]


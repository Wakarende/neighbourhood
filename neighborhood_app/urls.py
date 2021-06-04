from django.urls import path
# from .views import NeighbourhoodView
from .models import Neighbourhood
# from . import views

urlpatterns = [
  # path('', NeighbourhoodView.as_view(), name='neighbourhood'),
  # path('<int:id>/', NeighbourhoodView.as_view(), name='delete_neighbourhood'),
]

# urlpatterns = [
# 	path('', views.apiOverview, name="api-overview"),
# 	path('neighbourhood-list/', views.neigbourhoodList, name="neighbourhood-list"),
# 	path('neighbourhood-detail/<str:pk>/', views.neighbourhoodDetail, name="neighbourhood-detail"),
# 	path('neighbourhood-create/', views.neighbourhoodCreate, name="neighbourhood-create"),
# ]



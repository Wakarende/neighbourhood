from django.urls import path,re_path
from .models import BusinessModel
from .views import BusinessView,singleBusinessView

# app_name = 'business'

urlpatterns = [
  path('', BusinessView.as_view()),
  path('<int:pk>/', BusinessView.as_view()),
  path('get/<int:pk>/',singleBusinessView.as_view()),

  path('update/<int:pk>/', BusinessView.as_view()),
  path('delete/<int:pk>/', BusinessView.as_view()),
]
    

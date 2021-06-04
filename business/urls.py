from django.urls import path,re_path
# from .views import api_detail_business_view, api_update_business_view, api_delete_business_view,api_create_business_view
from .models import BusinessModel
from .views import BusinessView

# app_name = 'business'

urlpatterns = [
  path('', BusinessView.as_view()),
  path('<int:pk>/', BusinessView.as_view()),
  path('update/<int:pk>/', BusinessView.as_view()),
  path('delete/<int:pk>/', BusinessView.as_view()),
]
    

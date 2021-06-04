from django.urls import path,re_path
# from .views import api_detail_business_view, api_update_business_view, api_delete_business_view,api_create_business_view
from .models import BusinessModel
from .views import BusinessView

# app_name = 'business'

urlpatterns = [
  # path('', api_detail_business_view, name='business_detail'),
  path('', BusinessView.as_view(), name='business_detail'),
  # path('<int:id>/update', api_update_business_view, name='update'),
  # path('<int:id>/delete', api_delete_business_view, name='delete'),
  # path('create/', api_create_business_view, name='business_create'),
# re_path('update/<int:pk>/',BusinessView.as_view(),name='update_business'),
]
    

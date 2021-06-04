from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import BusinessSerializer
from rest_framework import serializers
from .models import BusinessModel
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render,HttpResponse,Http404
from rest_framework.decorators import api_view
from user.models import UserModel


# Create your views here.
# @api_view(['GET',])
# def api_detail_business_view(request, id):
#   try:
#     business = BusinessModel.objects.get(id=id)
#   except BusinessModel.DoesNotExist:
#     return Respone(status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'GET':
#     serializer=BusinessSerializer(business)
#     return Response(serializer.data)


# @api_view(['PUT',])
# def api_update_business_view(request, id):
#   try:
#     business = BusinessModel.objects.get(id=id)
#   except BusinessModel.DoesNotExist:
#     return Respone(status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'PUT':
#     serializer=BusinessSerializer(business, data=request.data)
#     data={}
#     if serializer.is_valid():
#       serializer.save()
#       data["success"]="update successful"
#       return Response(data=data)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE',])
# def api_delete_business_view(request, id):
#   try:
#     business = BusinessModel.objects.get(id=id)
#   except BusinessModel.DoesNotExist:
#     return Respone(status=status.HTTP_404_NOT_FOUND)

#   if request.method == 'DELETE':
#     operation = business.delete()
#     data={}
#     if operation:
#       data["sucess"]="delete successful"
    
#     else:
#       data["failure"]="delete failed"
      
#     return Response(data=data)

# @api_view(['POST',])
# def api_create_business_view(request):

#   user=UserModel.objects.get(pk=1)
#   business=BusinessModel(author=admin)

#   if request.method=="POST":
#     serializer= BusinessSerializer(business, data=request.data)
#     data={}
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serialzer.data, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class BusinessView(APIView):
#   serializer_class = BusinessSerializer
#   all_business = BusinessModel.objects.all()

#   def post(self, request, *args, **kwargs):
#     serializer = self.serializer_class(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     business_data = serializer.data

#     response = {
#       'data': {
#         'business': dict(business_data),
#         "status": "success",
#         "message": "Business created successfully"
#       }
#     }

#     return Response(response, status=status.HTTP_201_CREATED)

#   def get(self, request, *args, **kwargs):
#     serializers = BusinessSerializer(self.all_business, many=True)
#     return Response(serializers.data)

#   def get_business(self,pk):
#     try:
#       return Business.object.get(pk=pk)
#     except Business.DoesNotExist:
#         return Http404()


#   def put(self, request,pk, format=None):
#     business= self.get_business(pk)
#     serializers=BusinessSerializer(business, request.data)
#     if serializers.is_valid():
#       serializers.save()
#       all_business=serializers.dat
#       response={
#         'data':{
#           'business': dict(all_business),
#           'status': 'success',
#           'message': 'bussiness updated successfully.',
#         }
#       }


  
class BusinessView(APIView):
  serializer_class = BusinessSerializer
  all_business = BusinessModel.objects.all()

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    business_data = serializer.data

    response = {
      'data': {
        'business': dict(business_data),
        "status": "success",
        "message": "Business created successfully"
      }
    }

    return Response(response, status=status.HTTP_201_CREATED)

  def get(self, request, *args, **kwargs):
    serializers = BusinessSerializer(self.all_business, many=True)
    return Response(serializers.data)
    



    

from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import BusinessSerializer
from rest_framework import serializers
from .models import BusinessModel
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import render,HttpResponse,Http404
from rest_framework.decorators import api_view
# from user.models import UserModel


# Create your views here.
class BusinessView(APIView):
  serializer_class = BusinessSerializer
  all_business = BusinessModel.objects.all()
  model = BusinessModel
  
  def get_business(self, pk):
    try:
      return self.model.objects.get(pk=pk)
    except self.model.DoesNotExist:
      raise Http404

  def post(self, request, format=None, *args, **kwargs,):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_200_OK)

    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    business_data = serializers.data

    response = {
      'data': {
        'business': dict(business_data),
        "status": "success",
        "message": "Business created successfully"
      }
    }

    return Response(response, status=status.HTTP_200_OK)

  def get(self, request, *args, **kwargs):
    serializers = BusinessSerializer(self.all_business, many=True)
    return Response(serializers.data)

  def put(self, request, pk, format=None, *args, **kwargs):
    business = self.get_business(pk)
    serializers = BusinessSerializer(business, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None, *args, **kwargs):
    business = self.get_business(pk)
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class singleBusinessView(APIView):
  serializer_class = BusinessSerializer
  def get_business(self, pk):
    try:
      return BusinessModel.objects.get(pk=pk)
    except BusinessModel.DoesNotExist:
      return Http404()

  def get(self, request, pk, format=None):
    post = self.get_business(pk)
    serializers = self.serializer_class(post)
    return Response(serializers.data)

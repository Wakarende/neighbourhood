from django.shortcuts import render,HttpResponse,Http404
from .serializers import NeighbourhoodSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Neighbourhood
from django.http import response, JsonResponse
from rest_framework.decorators import api_view


# Create your views here.
class NeighbourhoodView(APIView):
  serializer_class = NeighbourhoodSerializer
  model = Neighbourhood

  def get_neighbourhood(self, pk,format=None):
    try:
      return Neighbourhood.objects.get(pk=pk)
    except Neighbourhood.DoesNotExist:
      raise Http404

  def get(self, request, format=None, *args, **kwargs):
    all_neighbourhoods = Neighbourhood.objects.all()
    serializers = self.serializer_class(all_neighbourhoods, many=True)
    return Response(serializers.data)

  def post(self, request, format=None, *args, **kwargs):
    serializers = NeighbourhoodSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None,*args, **kwargs):
    pk = self.kwargs.get('pk')
    neighbourhood = self.get_neighbourhood(pk)
    serializers = NeighbourhoodSerializer(neighbourhood, request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None, *args, **kwargs):
    neighbourhood = self.get_neighbourhood(pk)
    neighbourhood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  
class singleNeighbourhoodView(APIView):
  serializer_class = NeighbourhoodSerializer
  def get_neighbourhood(self, pk):
    try:
      return Neighbourhood.objects.get(pk=pk)
    except Neighbourhood.DoesNotExist:
      return Http404()

  def get(self, request, pk, format=None):
    post = self.get_neighbourhood(pk)
    serializers = self.serializer_class(post)
    return Response(serializers.data)


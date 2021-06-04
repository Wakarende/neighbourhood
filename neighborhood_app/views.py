from django.shortcuts import render,HttpResponse,Http404
from .serializers import NeighbourhoodClass
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Neighbourhood
from django.http import response, JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

# class NeighbourhoodView(APIView):
#   serializer_class = NeighbourhoodClass
#   all_neighbourhoods = Neighbourhood.objects.all()

#   def get_object(self, id):
#     try:
#       return Neighbourhood.objects.get(id=id)
#     except Neighbourhood.DoesNotExist as e:
#       return Response( {"error": "Given question object not found."}, status=404)

#   def post(self, request, *args, **kwargs):
#     serializer = self.serializer_class(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     neighbourhood_data = serializer.data

#     response = {
#       'data': {
#         'neighbourhood': dict(neighbourhood_data),
#         "status": "success",
#         "message": "Neighbourhood created successfully"
#       }
#     }

#     return Response(response, status=status.HTTP_201_CREATED)

#   def get(self, request, *args, **kwargs):
#     serializers = NeighbourhoodClass(self.all_neighbourhoods, many=True)
#     return Response(serializers.data)

#   def delete(self, request, id=None):
#     instance = self.get_object(id)
#     instance.delete()
#     return HttpResponse(status=204)
    
#   def put(self, request, id):
#     data = request.data
#     instance = self.get_object(id)
#     serializer = NeighbourhoodClass(instance, data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=200)
#     return Response(serializer.erros, status=400)


class NeighbourhoodApiView(APIView):
  def get(self,request):
    neighbourhoods = Neighbourhood.objects.all()
    serializer = NeighbourhoodClass(neighbourhoods,many=True)
    return Response(serializer.data, status=200)

  def post(self, request):
    data = request.data
    serializer = NeighbourhoodClass(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.erros, status=400)

# class NeighbourhoodDetailsView(APIView):
#   def get_object(self, id):
#     try:
#       return Neighbourhood.objects.get(id=id)
#       except Neighbourhood.DoesNotExist as e:
#         return Response({"error": "Given object not found"}, status=404)
#   def get(self, request, id=None):
#     instance=self.

# @api_view(['GET'])
# def apiOverview(request):
#   api_urls = {
#     'List':'/neighbourhood-list/',
#     'Detail View':'/neighbourhood-detail/<str:pk>/',
#     'Create':'/neighbourhood-create/',
#     'Update':'/neighbourhood-update/<str:pk>/',
#     'Delete':'/neighbourhood-delete/<str:pk>/',

#   }
#   return Response(api_urls)

# @api_view(['GET'])
# def neigbourhoodList(request):
# 	neighbourhoods = Neighbourhood.objects.all()
# 	serializer = NeighbourhoodClass(neighbourhoods, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def neighbourhoodDetail(request,pk):
# 	neighbourhoods = Neighbourhood.objects.get(id=pk)
# 	serializer = NeighbourhoodClass(neighbourhoods, many=False)
# 	return Response(serializer.data)

# @api_view(['POST'])
# def neighbourhoodCreate(request):
# 	serializer = NeighbourhoodClass(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

  # neighbourhood_data = serializer.data

    # response = {
    #   'data': {
    #     'neighbourhood': dict(neighbourhood_data),
    #     "status": "success",
    #     "message": "Neighbourhood created successfully"
    #   }
    # }
	# return Response(serializer.data)


  
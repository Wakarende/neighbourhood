from django.shortcuts import render
from .serializer import ProfileSerializer,UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.

class ProfileView(APIView):
  serializer_class=ProfileSerializer

  def get_profile(self, pk):
    try:
        return Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        raise Http404()
  
  def get(self, request, format=None, *args, **kwargs):
    profile = Profile.objects.all()
    serializers = self.serializer_class(profile, many=True)
    return Response(serializers.data)

  def post(self, request, format=None, *args, **kwargs):
    serializers = ProfileSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    profile = self.get_profile(pk)
    serializers = self.serializer_class(profile, request.data)
    if serializers.is_valid():
      serializers.save()
      profile_data = serializers.data
      response = {
          'data': {
              'profile': dict(profile_data),
              'status': 'success',
              'message': 'profile updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
  serializer_class=UserSerializer
  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None, *args, **kwargs):
    users=User.objects.all()
    serializers=self.serializer_class(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None, *args, **kwargs):
    serializers=self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()

      users=serializers.data
      response={
        'data':{
          'users':dict(users),
          'status':'success',
          'message':'user created successfully',
        }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,pk,format=None,*args, **kwargs):
    users=self.get_users(pk)
    serializers=self.serializer_class(users,request.data)
    if serializers.is_valid():
      serializers.save()
      users_list=serializers.data
      response = {
          'data': {
              'users': dict(users_list),
              'status': 'success',
              'message': 'user updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
  def delete(self,request,pk,format=None,*args, **kwargs):
    users=self.get_users(pk)
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
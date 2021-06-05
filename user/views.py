from django.shortcuts import render
from .serializer import ProfileSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.

# class UserRegistrationView(APIView):
#   serializer_class = UserSerializerClass
#   all_users = User.objects.all()
#   model = UserModel
    
#   def get_user(self, pk):
#     try:
#       return self.model.objects.get(pk=pk)
#     except self.model.DoesNotExist:
#       raise Http404

#   def post(self, request, *args, **kwargs):
#     serializer = self.serializer_class(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()

#     user_data = serializer.data

#     response = {
#       'data': {
#         "user": dict(user_data),
#         "status": "success",
#         "message": "Account created successfully"
#       }
#     }

#     return Response(response, status=status.HTTP_201_CREATED)

#   def get(self, request, *args, **kwargs):
#     serializers = UserSerializerClass(self.all_users, many=True)
#     return Response(serializers.data)
    
#   def post(self, request, format=None, *args, **kwargs):
#     serializers = UserSerializerClass(data=request.data)
#     if serializers.is_valid():
#       serializers.save()
#       return Response(serializers.data, status=status.HTTP_201_CREATED)
#     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#   def put(self, request, pk, format=None, *args, **kwargs):
#     user = self.get_user(pk)
#     serializers = UserSerializerClass(user, request.data)
#     if serializers.is_valid():
#       serializers.save()
#       return Response(serializers.data)
#     else:
#       return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


#   def delete(self, request, pk, format=None, *args, **kwargs):
#     user = self.get_user(pk)
#     user.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
  serializer_class=ProfileSerializer

  def get_profile(self, pk):
    try:
        return Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        raise Http404()
  
  def get(self, request, format=None):
    profile = Profile.objects.all()
    serializers = self.serializer_class(profile, many=True)
    return Response(serializers.data)

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

class UserList(APIView):
  serializer_class=UserSerializer
  def get_users(self,pk):
    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

  def get(self,request,format=None):
    users=User.objects.all()
    serializers=self.serializer_class(users, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
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

  def put(self,request,pk,format=None):
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
    
  def delete(self,request,pk,format=None):
    users=self.get_users(pk)
    users.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
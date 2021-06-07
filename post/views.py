from django.shortcuts import render
from .models import Post
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django.http import response
from rest_framework import filters
from .serializer import PostSerializer

# Create your views here.
class PostView(APIView):
  serializer_class=PostSerializer
  def get_post(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      raise Http404()

  def get(self, request, format=None,*args, **kwargs):
    post = Post.objects.all()
    serializers = self.serializer_class(post, many=True)
    return Response(serializers.data)

  

  def post(self, request, format=None,*args, **kwargs):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()

      post = serializers.data
      response = {
          'data': {
              'post': dict(post),
              'status': 'success',
              'message': 'post created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None,*args, **kwargs):
    post = self.get_post(pk)
    serializers = self.serializer_class(post, request.data)
    if serializers.is_valid():
      serializers.save()
      post_data = serializers.data
      response = {
          'data': {
              'post': dict(post_data),
              'status': 'success',
              'message': 'post updated successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None,*args, **kwargs):
    post = self.get_post(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class singlePostView(APIView):
  serializer_class = PostSerializer
  def get_post(self, pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return Http404()

  def get(self, request, pk, format=None):
    post = self.get_post(pk)
    serializers = self.serializer_class(post)
    return Response(serializers.data)
  
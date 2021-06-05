from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from django.db.models import fields
from business.serializer import BusinessSerializer
from django import forms
# class UserSerializerClass(serializers.ModelSerializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=6,
#                                      max_length=128,
#                                      write_only=True,
#                                      error_messages={
#                                          "min_length": "Password should be atleast {min_length} characters"
#                                      })
#     confirm_password = serializers.CharField(min_length=6,
#                                              max_length=128,
#                                              write_only=True,
#                                              error_messages={
#                                                  "min_length": "Password should be atleast {min_length} characters"
#                                              })

#     class Meta:
#         model = User
#         fields = ['id','username', 'email', 'password', 'confirm_password',]

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],

#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

class ProfileSerializer(serializers.ModelSerializer):
  # user=UserSerializer(read_only=True,many=False)
  business = BusinessSerializer(many=True, read_only=True)

  class Meta:
    model = Profile
    fields="__all__"


class UserSerializer(serializers.ModelSerializer):
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  class Meta:
    model = User
    fields = ['username','email','password']

from django.db import models
from django.db.models import fields
from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"
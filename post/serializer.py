from django.db import models
from django.db.models import fields
from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'post_name', 'post_content', 'pub_date','profile','neighbourhood')

    


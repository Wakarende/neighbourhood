from rest_framework import serializers
from .models import BusinessModel
from django.db import models


class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model=BusinessModel
    fields='__all__'


from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserModel(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(null=True)
  phone_number = models.CharField(max_length=10, null=True)

  def __str__(self):
    return self.user.username


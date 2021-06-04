from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class UserModel(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(null=True)
  phone_number = models.CharField(max_length=10, null=True)
  image=CloudinaryField('Profile Picture', default='')


  def __str__(self):
    return self.user.username

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  def edit_bio(self):
    self.bio=new_bio
    self.save()


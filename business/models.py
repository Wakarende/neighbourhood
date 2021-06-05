from django.db import models
from django.contrib.auth.models import User
from neighborhood_app.models import Neighbourhood
from user.models import Profile

# Create your models here.
class BusinessModel(models.Model):
  business_name = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,)
  business_email = models.EmailField()
    
  
  def __str__(self):
    return self.business_name
  
  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, business_name):
    return cls.objects.filter(name__icontains=business_name)

  @classmethod
  def update_business(cls, id, business_name):
    update = cls.objects.filter(id=id).update(name=business_name)
    return update


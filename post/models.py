from django.db import models
from user.models import Profile
from neighborhood_app.models import Neighbourhood

class Post(models.Model):
  post_name=models.CharField(max_length=100)
  post_content=models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  profile=models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='post',null=True)
  neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,related_name='post_hood',null=True)

  def __str__(self):
    return self.post_name

from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class reviews(models.Model):
  user_id = models.IntegerField()
  product_id = models.IntegerField()
  comment = models.CharField(max_length=1000)
  rating = models.IntegerField()


class node_user(models.Model):
  user_id = models.IntegerField()
  fb_id = models.IntegerField()
  user_name = models.CharField(max_length=20)

class edge_friend(models.Model):
  node_user_1 = models.IntegerField()
  node_user_2 = models.IntegerField()

class app_context(models.Model):
  key = models.CharField(max_length=10)
  value = models.CharField(max_length=100)


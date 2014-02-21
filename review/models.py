from django.db import models
# Create your models here.

from django.db import models

# Create your models here.
from allauth.socialaccount.models import SocialAccount
import hashlib
import urllib2, pycurl 
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
import httplib2, urllib

from allauth.socialaccount.models import SocialToken
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
 
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
 

    def profile_image_url(self):
      fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
      if len(fb_uid):
        return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

    def get_friend_list(self):
      fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
      at = SocialToken.objects.filter(account_id=self.user.id,app_id=2)
      import pdb;pdb.set_trace()
      params = {}
      params["access_token"] = at 
      if len(fb_uid):
        c= pycurl.Curl()
        url = "https://graph.facebook.com/"+format(fb_uid[0].uid)+"/friends"
        c.setopt(pycurl.URL, url)
        c.setopt(pycrul.HTTPHEADER, ['Accept: application/json'])
        c.setopt(pycurl.VERBOSE, 0)
        at = 'access_token:'+at
        c.setopt(pycurl.USERPWD, at)
        c.perform()

 #       params = urllib.urlencode(params)
#        result = urllib2.urlopen("https://graph.facebook.com/"+format(fb_uid[0].uid)+"/friends",params)
     # return result


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class node_user(models.Model):
  user_id = models.AutoField(primary_key=True)
  fb_id = models.CharField(max_length=20)
  user_name = models.CharField(max_length=20)

class reviews(models.Model):
  product_id = models.IntegerField()
  user_id = models.ForeignKey(node_user)
  comment = models.CharField(max_length=1000)
  rating = models.IntegerField()

  def getAllReview(self,product_id):
    return reviews.objects.filter(product_id=product_id)

  def getReviewForUserFriends(self,product_id,user_id):
      friends = edge_friend.objects.filter(node_user_1 =  user_id)
      rev_list = []
      rev_list_not =  self.getAllReview(product_id)
      for x in friends:
	rev_list += reviews.objects.filter(product_id=product_id).filter(user_id = x.node_user_2)
        rev_list_not = rev_list_not.exclude(user_id=x.node_user_2)

      return rev_list, rev_list_not

class edge_friend(models.Model):
#  node_user_1 = models.IntegerField()
#  node_user_2 = models.IntegerField()
   node_user_1 = models.ForeignKey(node_user,related_name = 'user1')
   node_user_2 = models.ForeignKey(node_user,related_name = 'user2')
   class Meta:
     unique_together = (("node_user_1", "node_user_2"),)

class app_context(models.Model):
  key = models.CharField(max_length=10)
  value = models.CharField(max_length=100)




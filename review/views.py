from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from review.models import *

def index(request):
    print request.user.profile.get_friend_list()
    return render(request, 'review/index.html')

def list_products(request, product_id):
    r = reviews()
    rev_list = r.getAllReview(product_id)
    if(not rev_list):
      return HttpResponse("No Reviews of the Product for product id %s." % product_id)
    else:
      return render(request, 'review/comments.html', {'rev_list': rev_list})

def list_products_trust(request, product_id,user_id):
    r = reviews()
    rev_list,rev_list_not = r.getReviewForUserFriends(product_id,user_id)
    if(not rev_list and not rev_list_not):
      return HttpResponse("No Reviews of the Product for product id %s." % product_id)
    else:
      return render(request, 'review/comments_trusted.html', {'rev_list': rev_list,'rev_list_not': rev_list_not})

    


def logout_view(request):
    logout(request)
    # Redirect to a success page.





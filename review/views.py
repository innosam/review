from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def list_products(request, product_id):
    return HttpResponse("List Reviews of the Product for product id %s." % product_id)


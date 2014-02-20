from django.conf.urls import patterns, url, include
from review import views

urlpatterns = patterns('',
   url(r'^$', views.index, name='index'),
   url(r'^(?P<product_id>\d+)/reviews/$',views.list_products,name='reviews'),
)

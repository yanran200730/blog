from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^wechat/$',views.wechat),
    url(r'^index/$',views.index),
    url(r'^demo1/$',views.demo1),
    url(r'^demo2/$',views.demo2)	
]
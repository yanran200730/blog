from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^wechat/$',views.wechat),
    url(r'^index/$',views.index),
    url(r'^demo1/$',views.demo1),
    url(r'^one/$',views.say),
    url(r'^shuo/$',views.shuo),
    url(r'^wechet_article/$',views.wechat_article),
    url(r'^code/$',views.code)

]
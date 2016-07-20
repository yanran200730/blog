from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^$',views.home,name="home"),
    url(r'^say/$',views.say,name="say"),
    url(r'^talk/$',views.talk,name="talk"),
    url(r'^like_count/$',views.like_count,name="like_count"),
    url(r'^shuoshuo/$',views.shuoshuo,name="shuoshuo"),
    url(r'^shuoshuo/Letter-(?P<id>[0-9]{1,})/$',views.mood,name ="Letter"),
    url(r'^article/$',views.article,name="article"),
    url(r'^article/blog-(?P<id>[0-9]{1,})/$',views.blog,name ="blog"),
    url(r'^music/$',views.music,name="music"),
    url(r'^learn/$',views.learn,name="learn"),
    url(r'^learn/article_coding-(?P<id>[0-9]{1,})/$',views.coding,name ="coding"),
    url(r'^zan/$',views.zan,name="zan"),
    url(r'^mobile$',views.mobile)
]
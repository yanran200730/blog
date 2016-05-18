from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^test/(\d*)', views.text),
    url('^login/$',views.login,name="login"),
    url('^register/$',views.register,name="register"),
    url('^$',views.home,name="home"),
    url('^say/$',views.say,name="sya"),
    url('^talk/$',views.talk,name="talk"),
    url('^like_count/$',views.like_count,name="like_count"),
    url('^shuoshuo/$',views.shuoshuo,name="shuoshuo"),
]
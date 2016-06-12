from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^adminfjsdklfjdisfusfhdshf/', include(admin.site.urls)),
    url(r'',include('blog.urls'))
]

"""vedomosti2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Offshores.views import *
from Users.views import *
from django.conf import settings
from django.conf.urls import patterns


urlpatterns = [
    url(r'^vedadmin/', admin.site.urls),
    url(r'^$', home),
    url(r'^(?P<id>\d+)/$', detail),
    url(r'^user/logout/$', logout),
    url(r'^login/$', form),
    url(r'^user/login/$', login),
    url(r'^faq/$', faq),
]



if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

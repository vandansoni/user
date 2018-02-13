from django.conf.urls import  patterns,include, url
from django.contrib import admin
from user_mgmt import settings
from account.views import *



urlpatterns = patterns('',
    url(r'^register/$', register, name='register'),
    url(r'^login/$', logIn, name='login'),
    url(r'^home/$', home, name='home'),
    url(r'^logout/$', logOut, name='logout'), 
)
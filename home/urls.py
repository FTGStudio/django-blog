__author__ = 'mike'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^michaeldoranjr.com$', views.HomePageView, name='home'),
]
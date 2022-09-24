from unicodedata import name
from django.urls import path 
from . import views


urlpatterns = [
    path('',views.public_feed,name="feed"),
    path('add/',views.add_post,name="add"),
     path('register/',views.register,name="register")
]

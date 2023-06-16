from django.urls import path
from .views import *

urlpatterns = [
    path('startpage', startpage, name='startpage'),
    path('post_list', post_list, name='post_list'),
]
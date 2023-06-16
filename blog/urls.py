from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('startpage', startpage, name='startpage'),
    path('post_list', post_list, name='post_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
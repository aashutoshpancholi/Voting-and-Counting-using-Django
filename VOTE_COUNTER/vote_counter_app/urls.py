from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.VOTE_APP, name='VOTE_APP'),
    path('getquery', views.getquery, name='getquery'),
    path('sortdata', views.sortdata, name='sortdata')
]
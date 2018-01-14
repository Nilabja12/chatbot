from django.urls import path

from . import views

urlpatterns = [
        path('', views.Home, name='home'),
		path('post/', views.Post, name='post'),
		path('messages/', views.Messages, name='messages'),
]
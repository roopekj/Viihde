from django.urls import path

from . import views

urlpatterns = [
    path('', views.streamURL, name='streamURL'),
]

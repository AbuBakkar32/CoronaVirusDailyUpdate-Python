from django.urls import path

from Tracker import views

urlpatterns = [
    path('', views.index, name='index')
]

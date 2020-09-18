from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='asd'),
    path('add/<int:nr1>/<int:nr2>/', views.addition, name='addition'),
    path('sub/<int:nr1>/<int:nr2>/', views.subtraction, name='subtraction'),
    path('mul/<int:nr1>/<int:nr2>/', views.multiplication, name='multiplication'),
    path('div/<int:nr1>/<int:nr2>/', views.division, name='division'),
]

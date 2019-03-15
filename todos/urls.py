from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<id>/', views.details, name='details'),
    path('add', views.add, name='add'),
    path('delete/<id>/', views.delete, name='delete'),
    path('complete/<id>/', views.complete, name='complete'),
]

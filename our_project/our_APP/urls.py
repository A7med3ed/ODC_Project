from django.urls import path
from . import views

urlpatterns = [
    path('our_APP/', views.index, name='index'),
   
]





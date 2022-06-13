from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('vaccination', views.vaccination, name = 'vaccination'),
]
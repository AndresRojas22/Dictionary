from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello', views.SayHello),
    path('', views.Home, name='home'),
    path('result', views.search, name='result'),
]

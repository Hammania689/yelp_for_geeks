from django.urls import path
from . import views
from guts import views as gutView

urlpatterns = [
    path('home', gutView.test),
    path('profile', views.index),
    path('signup', views.register, name='signup'),
]
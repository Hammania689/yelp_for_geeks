from django.urls import path
from . import views
from guts import views as gutView

urlpatterns = [
    path('', gutView.index),
    path('profile', views.profile, name='profile'),
# ^accounts/(?P<user>[\w-]+)/profile/$
#     path(r'^profile/(?P<user>[\w-]+)/$', gutView.ProfileDetailView.as_view(), name='profile-detail'),
#     path(r'^accounts/(?P<user>[\w-]+)/profile/$', gutView.ProfileDetailView.as_view(), name='profile-detail'),
    # path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    # path('profile/<str:pk>/', gutView.ProfileDetailView.as_view(), name='profile-detail'),
    path('signup', views.register, name='signup'),
]
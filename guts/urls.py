from django.urls import path
from . import views
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
    ProfileDetailView
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='home'),
    # path(r'^accounts/(?P<user>[\w-]+)/profile/$', ProfileDetailView.as_view(), name='profile-detail'),
    # path('profile/<str:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    # path('', views.test),
]


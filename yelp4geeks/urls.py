from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('guts/', include('guts.urls')),
    path('admin/', admin.site.urls),
]
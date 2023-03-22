from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('resume12', include('resume12.urls')),
    path('admin/', admin.site.urls),
]
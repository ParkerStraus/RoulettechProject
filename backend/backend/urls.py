from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('myapp.urls')),  # Ensure 'myapp' is replaced with your actual app name
]


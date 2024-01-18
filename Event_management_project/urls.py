from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register/',include('user_authenticated.urls')),
    path('event/',include('Event_creation.urls')),
    path('',include('core.urls')),
]

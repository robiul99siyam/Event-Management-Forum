from django.urls import path
from . import views

#------------------- all data urls ---------------->

urlpatterns = [
    path('', views.EventCreationAll.as_view(),name='home'),
    path('details/<int:pk>/' , views.UserDetailsView.as_view(),name='details'),
]

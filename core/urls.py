from django.urls import path
from . import views

#------------------- all data urls ---------------->

urlpatterns = [
    path('', views.EventCreationAll.as_view(),name='home'),
    path('details/<int:pk>/' , views.UserDetailsView.as_view(),name='details'),
    path('about/', views.About.as_view(),name='about'),
    path('contact/' , views.ContactView.as_view(),name='contact'),
]

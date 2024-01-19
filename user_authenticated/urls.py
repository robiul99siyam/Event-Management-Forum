from django.urls import path 
from . import views


#============ make a url in Register form =====================================>
urlpatterns = [
    path('resgister/', views.RegisterView.as_view(),name='register'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogOutView,name='logout'),
]

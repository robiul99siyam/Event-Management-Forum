from django.urls import path 
from . import views


#============ make a url in Register form =====================================>
urlpatterns = [
    path('resgister/', views.register,name='register'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogOutView,name='logout'),
    path('edit/<int:id>/', views.Userupdate.as_view(),name='edit'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
]

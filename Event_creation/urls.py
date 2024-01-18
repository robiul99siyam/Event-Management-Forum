from django.urls import path
from . import views


#------------ views Event creation ------------------>
urlpatterns = [
    path('',views.Event_cration_view.as_view(),name='event_creation'),
    path('confirm/<int:id>/',views.confirm_event,name='confirm_data'),
    path('profile/',views.ProfileViewData.as_view(),name='profile'),
    path('Delete/<int:id>/', views.UserDeleteNow,name='delete'),
    path("staff_user/", views.staff_userView.as_view(),name='staff'),
    path("update/<int:pk>/", views.UpdateViewUser.as_view(),name='update'),
    path("confrim/", views.ConfirmDetailListView.as_view(),name='confrim'),
]


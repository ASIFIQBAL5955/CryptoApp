from django.urls import path
from . import views
urlpatterns = [

    path('', views.dashboardscreen , name= 'dashboardscreen'),
#     path('', views.changepassword , name = 'changepassword'),
#     path('', views.chatscreen , name = 'chatscreen'),
    path('chatscreen_Second', views.chatscreen_Second, name='chatscreen_Second'),
 
#     path('' , views.profile_Screen, name = 'profile_Screen'),
    path('refferalscreen', views.refferalscreen, name = 'refferalscreen'),
    path('socialaccounts', views.socialaccounts , name = 'socialaccounts'),
    path('unstable', views.unstable , name = 'unstablepage')
]
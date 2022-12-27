from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.dashboardscreen , name= 'dashboardscreen'),
    path('change_password', views.changepassword , name = 'changepassword'),
#     path('', views.chatscreen , name = 'chatscreen'),
    path('dashboard', views.dashboardscreen),
    path('chat_screen', views.chat_screen),
    path('change_psw', views.change_pswd),
    
    path('chatscreen_Second', views.chatscreen_Second, name='chatscreen_Second'),
 
#     path('' , views.profile_Screen, name = 'profile_Screen'),
    path('refferalscreen', views.refferalscreen, name = 'refferalscreen'),
    path('socialaccounts', views.socialaccounts , name = 'socialaccounts'),
    path('unstable', views.unstable , name = 'unstablepage')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
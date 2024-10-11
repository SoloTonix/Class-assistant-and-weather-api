from django.urls import path
from.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    path('register/', SignUp, name='SignUp'),
    path('login/', UserLogin, name='UserLogin'),
    path('logout/', UserLogout, name='UserLogout'),
    path('profile/', UserProfile, name='UserProfile'),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
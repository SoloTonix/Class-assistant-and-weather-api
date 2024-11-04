from django.urls import path  
from.views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # Admin URLS
    path('', Index, name='Index'),
    
    # Course URLS
    path('create-course/', CreateCourse, name='CreateCourse'),
    path('course-notes/<int:pk>/', CourseDetail, name='CourseDetail'),
    path('update-course/<int:pk>/', UpdateCourse, name='UpdateCourse'),
    path('delete-course/<int:pk>/', DeleteCourse, name='DeleteCourse'),
    path('search-course/', SearchCourse, name='SearchCourse'),

    # Course-Notes URLS 
    path('note/<int:pk>/', DetailNote, name='DetailNote'),
    path('create-note/<int:pk>/', CreateNote, name='CreateNote'),
    path('update/<int:pk>/', UpdateNote, name='UpdateNote'),
    path('delete/<int:pk>/', DeleteNote, name='DeleteNote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
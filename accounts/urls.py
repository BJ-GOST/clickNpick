from django.urls import path
from . import views 

urlpatterns = [
    path('register', views.register, name='register'),
    path('reader-login', views.reader_login, name='login'),
    path('reader-logout', views.reader_logout, name='logout')
]
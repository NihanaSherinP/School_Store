from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'schoolapp'

urlpatterns = [

    path('', views.home,name='home'),
    path('userhome', views.userhome,name='userhome'),




]

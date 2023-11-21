# orders/urls.py

from django.urls import path

from . import views
app_name='userseg'

urlpatterns = [

    path('order_page/', views.order_page, name='order_page'),
    path('getdata/',views.getdata,name="getdata"),
    path('getcourses/', views.getcourses, name='getcourses'),
    # Add more URL patterns as needed
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
     path('rooms/', views.roomspage, name='rooms'),
     path('home/',views.home,name='home'),
     path('login/',views.login,name='login'),
     path('signup/',views.signup,name='signup'),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('contactus/',views.contactus,name='contactus'),
     path('booking/',views.booking,name='booking'),
]




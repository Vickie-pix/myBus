from django.urls import path
from . import views


urlpatterns=[
     path('trip/', views.trippage, name='trip'),
     path('home/',views.home,name='home'),
     path('login/',views.login,name='login'),
     path('signup/',views.signup,name='signup'),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('services/',views.services,name='services'),
     path('contactus/',views.contactus,name='contactus'),
     path('trip/',views.trippage,name='trip'),
     path('bus/',views.buspage,name='bus'),
     path('billing/',views.billingpage,name='billing'),
     path('booking/',views.booking,name='booking'),
   
]



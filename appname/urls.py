from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events1/', views.events1, name='events1'),
    path('events2/', views.events2, name='events2'),
    path('events3/', views.events3, name='events3'),
     path('events4/', views.events4, name='events4'),
    path('events5/', views.events5, name='events5'),
    path('events6/', views.events6, name='events6'),
    path('register/', views.register, name='register'),
    path('contactus/', views.contactus, name='contactus'),
    path('location/', views.location, name='location'),
]

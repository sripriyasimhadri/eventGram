from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

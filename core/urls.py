from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    # path('register', views.register, name='register'),
]

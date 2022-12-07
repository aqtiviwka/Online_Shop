from django.contrib import admin
from django.urls import path
from main import views
from authentication import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),

]

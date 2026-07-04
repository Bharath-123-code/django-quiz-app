from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('debug-deploy/', views.debug_deploy, name='debug_deploy'),
]
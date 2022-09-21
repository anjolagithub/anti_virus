from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="loginpage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutpage, name="logoutpage"),
]

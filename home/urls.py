from django.urls import path

from home import create_meta
from . import views

urlpatterns = [
    path('', views.home),
    path('meta/s/project', create_meta.submitProjects, name="submitProjects"),
    path('meta/s/meta', create_meta.create_meta, name="createMeta"),
    path('subcribe', views.feedback),
    path('soap', create_meta.create_profile),
    path('meta/profile', views.profile, name="profile"),
    path('meta/project', views.projects, name="project"),
    path('meta/metas', views.metas, name="metas"),
    path('meta', views.choice, name ="meta"),
    path('login/', views.loginpage, name="loginpage"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutpage, name="logoutpage"),
]

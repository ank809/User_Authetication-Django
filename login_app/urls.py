from django.urls import path 
from . import views
urlpatterns=[
    path('login_page/', views.login_user, name="login_page"),
    path('home_page', views.home_page, name='home_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user')
]
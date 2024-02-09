from django.urls import path 
from . import views
urlpatterns=[
    path('login_page/', views.login_user, name="login_page"),
    path('home_page', views.home_page, name='home_page')
]
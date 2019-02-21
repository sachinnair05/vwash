from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns=[
    url('login', views.adminpage, name="login"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('logout',views.logout, name='logout')
]
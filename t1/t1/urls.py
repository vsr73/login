"""t1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main',views.mainpage),
    path('signup', views.signup),
    path('login/', views.login,name='login'),
    path('login/login', views.login),
    path('logout', views.logout),
    path('',views.mainpage),
    path('test',views.test),
    path('update/<str:pk>/',views.edit, name ='updateuser'),
    path('delete/<str:pk>/',views.delete,name='deleteuser'),
    path('upd/<str:pk>/',views.edit,name='upduser'),
    path('dlt/<str:pk>/',views.delete,name='dltuser')
]

"""mstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from studentdemo.views import index
from studentdemo.views import student
from studentdemo.views import degree
from studentdemo.views import httres
from studentdemo.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', index, name='index'),
    path('', student, name='student'),
    path('degree/<str:student_id>/', degree, name='degree'),
    path('httres/',httres, name='http' ),
    path('register/',register, name='register' )

]

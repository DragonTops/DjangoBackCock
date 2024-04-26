from django.urls import path

from . import views

urlpatterns = [
    path("enteraccount/", views.createUser, name="createUser"),
    path("loginUser/", views.loginUser, name="loginUser"),
    path("getData/", views.getData, name="getData"),
    path("", views.index, name="index")
]
from django.urls import path

from . import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("sell",views.sell,name="sell"),
    path("sell_form",views.sell_form,name="sell_form"),
]














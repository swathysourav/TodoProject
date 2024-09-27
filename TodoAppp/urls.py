from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home-page"),
    path('logout/', views.logout_view,name="logout"),
    path('register/', views.register,name="register"),
    path('login/', views.loginpage,name="login"),
    path('delete/<str:title>/', views.delete,name="delete"),
    path('update/<str:title>/', views.update,name="update"),
]
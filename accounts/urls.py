from django.urls import path
from . import views
urlpatterns = [
    path('/login', views.login,name='login-page'),
    path('/register', views.register,name='register-page'),

]
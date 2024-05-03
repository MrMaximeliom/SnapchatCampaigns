from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login,name='login-page'),
    path('logout', views.logout,name='logout-page'),
    path('register', views.register,name='register-page'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('validate_password/', views.validate_password, name='validate_password'),

]

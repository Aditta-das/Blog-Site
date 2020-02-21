from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/signin', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('new_register/', views.new_register, name='new_register'),
]
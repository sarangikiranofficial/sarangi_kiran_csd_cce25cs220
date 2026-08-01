from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    
    path('dresses/', views.dress_list, name='dress_list'),
    path('dresses/add/', views.add_dress, name='add_dress'),
    path('dresses/edit/<int:pk>/', views.edit_dress, name='edit_dress'),
    path('dresses/delete/<int:pk>/', views.delete_dress, name='delete_dress'),
]
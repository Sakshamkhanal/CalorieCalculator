from django.urls import path,include
from . import views
from django.contrib.auth import views as aith_views

urlpattern =[
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'),
    path('product/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.home,name='logout'),
    path('addFooditem/',views.addFooditem,name='addFooditem'),
    path('reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordRestDoneView.as_view(),name='password_reset_done'),
    path('reset_password_sent/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
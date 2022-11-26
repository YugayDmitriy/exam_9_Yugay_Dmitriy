from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login', views.login_page, name='login-page'),
    path('register', views.userregister, name='register-page'),
    path('save_register', views.save_register, name='register-user'),
    path('user_login', views.login_user, name='login-user'),
    path('logout', views.logout_user, name='logout'),
    path('profile', views.profile, name='profile-page'),
    path('update_profile', views.update_profile, name='update-profile'),
    path('update_password', views.update_password, name='update-password'),
]
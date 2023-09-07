from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name="Logout"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="Login"),
    path('settings/password_reset/', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html'), name="password_change"),
    path('settings/password_reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/change_password_done.html'), name="password_change_done"),
]
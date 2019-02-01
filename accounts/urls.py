from django.urls import path
from django.contrib.auth import views as auth_views #handles the log in/log out automatically
from .import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'), #need to supply template html
    path('logout/', auth_views.LogoutView.as_view(),name='logout'), #uses a default view
    path('signup/', views.SignUp.as_view(), name='signup'),

]
from django.urls import path
from django.contrib.auth import views as authviews
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',authviews.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',authviews.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup')
    ]
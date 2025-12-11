from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
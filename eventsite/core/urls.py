from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('testing/', views.testing, name='test'),
    path('test_db/', views.test_db, name='test_db'),
]
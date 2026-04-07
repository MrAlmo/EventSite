from django.urls import path, include
from . import views

urlpatterns = [
    path('join/<int:event_id>/', views.register_for_event, name='register_for_event'),
    path('leave/<int:event_id>/', views.cancel_registration, name='cancel_registration'),
]

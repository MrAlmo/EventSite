from django.urls import path
from .views import add_feedback

urlpatterns = [
    path('add/<int:event_id>/', add_feedback, name='add_feedback'),
]
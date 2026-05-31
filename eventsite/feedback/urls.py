from django.urls import path
from .views import add_feedback, delete_feedback

urlpatterns = [
    path('add/<int:event_id>/', add_feedback, name='add_feedback'),
    path('del/<int:event_id>/', delete_feedback, name='delete_feedback'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('e', views.events, name='events'),
    path('', views.EventListView.as_view(), name='event_list'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/edit', views.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name='event-delete'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
]
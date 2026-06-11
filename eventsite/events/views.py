from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from registrations.models import Registration
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .forms import EventForm
from feedback.forms import FeedbackForm
from rest_framework.views import APIView
from .serializers import EventSerializer, RegistrationSerializer
from rest_framework.response import Response



def events(request):
    return render(request, 'events/events.html')

class ModeratorRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_authenticated() and self.request.uset.is_moderator

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/event_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()

        context['upcoming_events'] = Event.objects.filter(date_time__gte=now).order_by('date_time')

        context['past_events'] = Event.objects.filter(date_time__lt=now).order_by('-date_time')

        return context

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_registered'] = Registration.objects.filter(
                user=self.request.user,
                event=self.get_object()
            ).exists()
            context['feedback_form'] = FeedbackForm()
        return context

class EventCreateView(CreateView, LoginRequiredMixin, ModeratorRequiredMixin):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(EventCreateView, self).form_valid(form)

    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView, LoginRequiredMixin, ModeratorRequiredMixin):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def test_func(self):
        event = self.get_object()
        return event.creator == self.request.user and self.request.user.is_moderator

class EventDeleteView(DeleteView, LoginRequiredMixin, ModeratorRequiredMixin):
    model = Event
    success_url = reverse_lazy('event_list')
    template_name = 'events/event_delete.html'

    def test_func(self):
        event = self.get_object()
        return event.creator == self.request.user and self.request.user.is_moderator

class ParticipantDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_participants.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = self.object.attendees.all()
        return context

class UpcomingEventsAPI(APIView):
    def get(self, request):
        now = timezone.now()
        events = Event.objects.filter(date_time__gte=now).order_by('date_time')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class MyEventsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        registrations = request.user.registrations.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
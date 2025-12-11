from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Event
from .forms import EventForm


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

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_detail.html'

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
    template_name = 'events/event_update.html'

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
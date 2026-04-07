from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.models import Event
from .models import Registration


@login_required
def register_for_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if Registration.objects.filter(user=request.user, event=event).exists():
        messages.info(request, "You are already registered for this event.")
        return redirect('event_detail', pk=event.id)

    if event.max_attendance > 0:
        current_count = event.attendees.count()
        if current_count >= event.max_attendance:
            messages.error(request, "Sorry, this event is full!")
            return redirect('event_detail', pk=event.id)


    Registration.objects.create(user=request.user, event=event)
    messages.success(request, f"Successfully registered for {event.title}!")

    return redirect('event_detail', pk=event.id)


@login_required
def cancel_registration(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    registration = Registration.objects.filter(user=request.user, event=event)

    if registration.exists():
        registration.delete()
        messages.success(request, "Your registration has been cancelled.")
    else:
        messages.error(request, "You were not registered for this event.")

    return redirect('event_detail', pk=event.id)

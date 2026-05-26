from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from events.models import Event

from .forms import FeedbackForm


@login_required
def add_feedback(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.event = event
            feedback.save()
            messages.success(request, 'Your feedback has been submitted.')
        return redirect('event_detail', pk=event.id)

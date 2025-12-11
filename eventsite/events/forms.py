from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    date_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
                                    label='Date/Time')

    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date_time', 'max_attendance']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:ring-indigo-500 focus:border-indigo-500'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:ring-indigo-500 focus:border-indigo-500'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:ring-indigo-500 focus:border-indigo-500'}),
            'max_attendees': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg focus:ring-indigo-500 focus:border-indigo-500'}),
        }
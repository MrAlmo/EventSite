from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'w-full p-3 border rounded-lg', 'rows': 4}),
            'rating': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'w-full p-2 border rounded'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 5}))
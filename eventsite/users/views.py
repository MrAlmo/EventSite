from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import CustomUser
from rest_framework.authtoken.models import Token


class SignUpView(CreateView):

    form_class = CustomUserCreationForm

    success_url = reverse_lazy('login')

    template_name = 'users/register.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_events'] = self.request.user.registrations.all().order_by('-registered_at')
        token, created = Token.objects.get_or_create(user=self.request.user)
        context['token'] = token.key
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
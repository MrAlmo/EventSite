from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from users.models import CustomUser
from .forms import ContactForm


def home(request):
    template = loader.get_template('core/home.html')
    return render(request, 'core/home.html')

def testing(request):
    template = loader.get_template('core/test.html')
    return HttpResponse(template.render())

def test_db(request):
    c_user = CustomUser.objects.all().values()
    context = {
        'c_users': c_user,
    }
    return render(request, 'core/test_db.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email= form.cleaned_data['email']
            name = form.cleaned_data['name']

            send_mail(subject=f'Message from site: {subject}', message=f'From {name} / {email} \n\n {message}',from_email='backford6@gmail.com', recipient_list=['backford6@gmail.com'], fail_silently=True)
            messages.success(request, 'Your message has been sent.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
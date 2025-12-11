from django.shortcuts import render, HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('core/home.html')
    return render(request, 'core/home.html')

def testing(request):
    template = loader.get_template('core/test.html')
    return HttpResponse(template.render())
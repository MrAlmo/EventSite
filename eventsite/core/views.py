from django.shortcuts import render, HttpResponse
from django.template import loader
from users.models import CustomUser


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
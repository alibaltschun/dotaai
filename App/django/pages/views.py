from django.shortcuts import render
from .utils.drafting import set_up
from .utils.user_data import read_user_data
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse


def home(request):
    template = 'empty.html'
    propt = read_user_data()

    if propt['ui'] == 'drafting':
        propt = set_up()
        template = 'drafting/main.html'

    if propt['ui'] == 'gameplay':
        propt = {
            'notifications': [
                {
                    'text': 'test',
                    'id': 0,
                    'delay': 500
                }
            ]
        }
        template = 'gameplay/main.html'

    return render(request, template, propt)


def create_user(request):
    try:
        # _ = User.objects.create_user(username='test',
        #                                 email='tes@test.com',
        #                                 password='test')
        u = User.objects.get(email='tes@test.com')
        print(u)
        return HttpResponse(200)
    except Exception as e:
        print(e)
        return HttpResponse(400)

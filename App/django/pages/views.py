from django.shortcuts import render
from .utils.drafting import set_up
from .utils.user_data import read_user_data


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

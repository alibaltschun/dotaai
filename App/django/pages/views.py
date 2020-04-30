from django.shortcuts import render
from .utils.drafting import set_up


def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def drafting(request):
    template = 'drafting/main.html'

    propt = set_up()

    return render(request, template, propt)

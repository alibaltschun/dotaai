from django.shortcuts import render
from .utils import hero, stat_meta, stat_most_played, stat_win_rate


def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def drafting(request):
    template = 'drafting/main.html'

    radiant = ['Bristleback', 'Sniper', 'Lion', 'Warlock', 'Pudge']
    dire = ['Axe', 'Bloodseeker', 'Razor', 'Zeus', 'Necrophos']

    radiant_data, dire_data = hero(radiant, dire)

    propt = {
        'radiant_heros': radiant_data,
        'dire_heros': dire_data,
        'statistics': [
            stat_meta(123),
            stat_meta(4),
            stat_meta(5),
            stat_meta(6),
            stat_meta(78),
            stat_win_rate(),
            stat_most_played(),
        ]
    }

    return render(request, template, propt)

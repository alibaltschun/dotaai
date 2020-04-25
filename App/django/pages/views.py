from django.shortcuts import render
from .utils import (
    hero,
    stat_meta,
    stat_most_played,
    stat_win_rate,
    summary_atribute
)


def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def drafting(request):
    template = 'drafting/main.html'

    radiant = ['Bristleback', 'Sniper', 'unselection', 'Warlock', 'Pudge']
    dire = ['Axe', 'Bloodseeker', 'unselection', 'unselection', 'Necrophos']

    radiant_data, dire_data = hero(radiant, dire)

    s_r_attack, s_r_armor, s_r_speed = summary_atribute(radiant_data)

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
        ],
        'summary': {
            'attack': s_r_attack,
            'armor': s_r_armor,
            'movement': s_r_speed
        }
    }

    print(s_r_speed)

    return render(request, template, propt)

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
        ],
        'summary': {
            'attack': [
                {
                    'name': 'Zeus',
                    'attack_min': 1,
                    'attack_max': 2
                },
                {
                    'name': 'Lina',
                    'attack_min': 3,
                    'attack_max': 4
                },
                {
                    'name': 'Luna',
                    'attack_min': 5,
                    'attack_max': 6
                },
                {
                    'name': 'Razor',
                    'attack_min': 7,
                    'attack_max': 8
                },
                {
                    'name': 'Lion',
                    'attack_min': 90,
                    'attack_max': 10
                }
            ],
            'armor': [
                {
                    'name': 'Zeus',
                    'armor': 2
                },
                {
                    'name': 'Lina',
                    'armor': 4

                },
                {
                    'name': 'Luna',
                    'armor': 2

                },
                {
                    'name': 'Razor',
                    'armor': 3

                },
                {
                    'name': 'Lion',
                    'armor': 5

                }
            ],
            'movement': [
                {
                    'name': 'Zeus',
                    'movement_speed': 100,
                },
                {
                    'name': 'Lina',
                    'movement_speed': 100,
                },
                {
                    'name': 'Luna',
                    'movement_speed': 100,
                },
                {
                    'name': 'Razor',
                    'movement_speed': 100,
                },
                {
                    'name': 'Lion',
                    'movement_speed': 100,
                }
            ]
        }
    }

    return render(request, template, propt)

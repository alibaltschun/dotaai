from django.shortcuts import render
from .utils import hero


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
            {
                'id': 'hero_meta_123',
                'title': 'Top 5 Heros base on meta',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                    },
                ]
            },
            {
                'id': 'hero_meta_4',
                'title': 'Top 5 Heros base on meta',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                    },
                ]
            },
            {
                'id': 'hero_meta_5',
                'title': 'Top 5 Heros base on meta',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                    },
                ]
            },
            {
                'id': 'hero_meta_6',
                'title': 'Top 5 Heros base on meta',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                    },
                ]
            },
            {
                'id': 'hero_meta_78',
                'title': 'Top 5 Heros base on meta',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                    },
                ]
            },
            {
                'id': 'hero_win_rate',
                'title': 'Top 5 Heros base on win rate',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                        'kill_date_ratio': 1,
                    },
                ]
            },
            {
                'id': 'hero_most_played',
                'title': 'Top 5 Heros base on most played',
                'heros': [
                    {
                        'name': 'Lina',
                        'win_rate': 51,
                        'pick_rate': 52,
                        'kill_date_ratio': 1,
                        'matches_played': 51,
                    },
                ]
            }
        ]
    }

    return render(request, template, propt)

from django.shortcuts import render


def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def drafting(request):
    template = 'drafting/main.html'

    propt = {
        'radiant_heros': [

            {
                'name': 'Zeus',
                'strength': 25,
                'agility': 14,
                'intelligence': 16,
                'attack_min': 65,
                'attack_max': 71,
                'armor': 0,
                'movement': 280,

                'work_well_with': [
                    'Lion'
                ],

                'good_against': [
                    'Lina',
                    'Lion'
                ],

                'Bad_against': [
                    'Lina',
                    'Lion',
                    'Crystal_Maiden'
                ]
            }
        ]
    }

    return render(request, template, propt)

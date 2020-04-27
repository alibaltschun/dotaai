from django.shortcuts import render
from .utils import (
    hero,
    stat_meta,
    stat_most_played,
    stat_win_rate,
    summary_atribute,
    summary_attack_abilities,
    summary_countered
)


def home(request):
    template = 'home.html'

    propt = {}

    return render(request, template, propt)


def __setup_show_ui_stat__(id_show):
    stats = [ 
        stat_meta(123),
        stat_meta(4),
        stat_meta(5),
        stat_meta(6),
        stat_meta(78),
        stat_win_rate(),
        stat_most_played(),
    ]

    for stat in stats:
        stat['show'] = False

    if id_show >= 0 and id_show < 7:
        stats[id_show]['show'] = True

    return stats


def __setup_show_ui_hero_info(radiant_data, dire_data, arr_show):
    for i in range(5):
        radiant_data[i]['show_info'] = arr_show[i]

    for i in range(5):
        dire_data[i]['show_info'] = arr_show[i+5]

    return radiant_data, dire_data


def drafting(request):
    template = 'drafting/main.html'

    radiant = ['Bristleback', 'Sniper', 'Lion', 'Warlock', 'Pudge']
    dire = ['Axe', 'Bloodseeker', 'Razor', 'Zeus', 'Necrophos']

    radiant_data, dire_data = hero(radiant, dire)

    s_r_attack, s_r_armor, s_r_speed = summary_atribute(radiant_data)
    s_r_attack_type, s_r_demage_type = summary_attack_abilities(radiant)
    s_r_countered = summary_countered(radiant)

    s_d_attack, s_d_armor, s_d_speed = summary_atribute(dire_data)
    s_d_attack_type, s_d_demage_type = summary_attack_abilities(dire)
    s_d_countered = summary_countered(dire)

    arr_show_hero_info = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    radiant_data, dire_data = __setup_show_ui_hero_info(
                                    radiant_data,
                                    dire_data,
                                    arr_show_hero_info)

    stats = __setup_show_ui_stat__(id_show=6)

    propt = {
        'radiant_heros': radiant_data,
        'dire_heros': dire_data,
        'statistics': stats,
        'summary': [
            {
                'name': 'Radiant',
                'position': 'left',
                'attack': s_r_attack,
                'armor': s_r_armor,
                'movement': s_r_speed,
                'abilities': {
                    'attack_type': {
                        'key': s_r_attack_type[0],
                        'value': s_r_attack_type[1]
                    },
                    'demage_type': {
                        'key': s_r_demage_type[0],
                        'value': s_r_demage_type[1]
                    },
                },
                'countered': s_r_countered,
                'settings':{
                    'show_ui': {
                        'main': True,
                        'recomendation_countering': False,
                        'abilitites': True,
                    }
                }
            },
            {
                'name': 'Dire',
                'position': 'right',
                'attack': s_d_attack,
                'armor': s_d_armor,
                'movement': s_d_speed,
                'abilities': {
                    'attack_type': {
                        'key': s_d_attack_type[0],
                        'value': s_d_attack_type[1]
                    },
                    'demage_type': {
                        'key': s_d_demage_type[0],
                        'value': s_d_demage_type[1]
                    },
                },
                'countered': s_d_countered,
                'settings':{
                    'show_ui': {
                        'main': False,
                        'recomendation_countering': True,
                        'abilitites': False,
                    }
                }
            }
        ]
    }

    print(s_r_speed)

    return render(request, template, propt)

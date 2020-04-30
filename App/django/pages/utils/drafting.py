import json
import os
import pandas as pd
from collections import Counter
from .user_data import read_user_data
BASE = (os.path.dirname(os.path.realpath(__file__)))

DATA_HERO = pd.read_csv(BASE + "/../../static/csv/hero.csv")
DATA_STAT_WIN_RATE = pd.read_csv(
    BASE + "/../../static/csv/hero_win_top5.csv")
DATA_STAT_MOST_PLAYED = pd.read_csv(
    BASE + "/../../static/csv/hero_most_played_top5.csv")
DATA_STAT_META = pd.read_csv(
    BASE + "/../../static/csv/hero_meta.csv")


def __rounding__(i):
    return round(float(i), 2)


def __str2arr__(heros):
    str1 = heros.replace(']', '').replace('[', '').replace(" '", "")
    str1 = str1.replace("'", "").replace(" ", "_")
    return str1.replace('"', '').split(",")


def __get_hero_data__(heros, df, index):
    data = []
    for hero in heros:
        if hero.lower() != "unselection":
            hero_data = df.loc[df['Hero'] == hero]

            data.append({
                'index': index,
                'show_info': False,
                'name': hero,
                'strength': int(hero_data['STR']),
                'agility': int(hero_data['AGI']),
                'intelligence': int(hero_data['INT']),
                'attack_min': int(hero_data['DMG (MIN)']),
                'attack_max': int(hero_data['DMG (MAX)']),
                'armor': int(hero_data['AR']),
                'movement': int(hero_data['MS']),

                'work_well_with': __str2arr__(
                    hero_data['Works well with'].item()),
                'good_against': __str2arr__(hero_data['Good against'].item()),
                'bad_against': __str2arr__(hero_data['Bad against'].item())
            })

        else:
            data.append({
                'index': index,
                'invisible': 'invisible'
            })

        index += 1

    return data, index


def __setup_show_ui_stat__(id_show):
    stats = [
        __stat_meta__(123),
        __stat_meta__(4),
        __stat_meta__(5),
        __stat_meta__(6),
        __stat_meta__(78),
        __stat_win_rate__(),
        __stat_most_played__(),
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


def __hero__(radiant, dire, df=DATA_HERO):
    index = 0

    radiant_data, index = __get_hero_data__(radiant, df, index)
    dire_data, index = __get_hero_data__(dire, df, index)

    return radiant_data, dire_data


def __stat_meta__(meta_id, df=DATA_STAT_META):
    _id = "hero_meta_"+str(meta_id)
    _title = "Top 5 Heros base on meta"

    df_meta = df.sort_values(
        'rank {} win'.format(meta_id),
        ascending=False)[:5]

    df_meta = df_meta[[
        'Hero',
        'rank {} win'.format(meta_id),
        'rank {} pick'.format(meta_id)]]

    heros = []
    for index, row in df_meta.iterrows():
        heros.append({
            'name': row[0].replace(" ", "_"),
            'win_rate': __rounding__(row[1]),
            'pick_rate': __rounding__(row[2])
            })

    result = {
        'id': _id,
        'title': _title,
        'heros': heros
        }

    return result


def __stat_win_rate__(df=DATA_STAT_WIN_RATE):
    _id = "hero_win_rate"
    _title = "Top 5 Heros base on win rate"

    heros = []
    for index, row in df.iterrows():
        heros.append({
            'name': row['Hero'].replace(" ", "_"),
            'win_rate': __rounding__(row['Win Rate']),
            'pick_rate': __rounding__(row['Pick Rate']),
            'kill_date_ratio': __rounding__(row['KDA Ratio']),
            })

    result = {
        'id': _id,
        'title': _title,
        'heros': heros
        }

    return result


def __stat_most_played__(df=DATA_STAT_MOST_PLAYED):
    _id = "hero_most_played"
    _title = "Top 5 Heros base on most played"

    heros = []
    for index, row in df.iterrows():
        heros.append({
            'name': row['Hero'].replace(" ", "_"),
            'win_rate': __rounding__(row['Win Rate']),
            'pick_rate': __rounding__(row['Pick Rate']),
            'kill_date_ratio': __rounding__(row['KDA Ratio']),
            'matches_played': row['Matches Played'],
            })

    result = {
        'id': _id,
        'title': _title,
        'heros': heros
        }

    return result


def __summary_atribute__(heros):
    df = pd.DataFrame(heros)
    df = df[df['name'].notna()]

    df_attack = df.sort_values(
        'attack_max', ascending=False)[['name', 'attack_min', 'attack_max']]
    df_armor = df.sort_values(
        'armor', ascending=False)[['name', 'armor']]
    df_speed = df.sort_values(
        'movement', ascending=False)[['name', 'movement']]

    attack = json.loads(df_attack.to_json(orient='records').replace('.0', ''))
    armor = json.loads(df_armor.to_json(orient='records').replace('.0', ''))
    speed = json.loads(df_speed.to_json(orient='records').replace('.0', ''))

    return attack, armor, speed


def __summary_countered__(heros, df=DATA_HERO):
    bad_against = []
    df = df.loc[df['Hero'].isin(heros)]

    for row in df['Bad against']:
        str1 = row.replace(']', '').replace('[', '').replace(" '", "")
        str1 = str1.replace("'", "").replace(" I", "I")

        for i in str1.replace('"', '').split(","):
            if i != "":
                bad_against.append(i)

    max_countered = max(list(Counter(bad_against).values()))
    summary_countered = [[i, []] for i in range(1, max_countered)]

    for i in range(len(Counter(bad_against).keys())):
        total_countred = list(Counter(bad_against).values())[i]
        if total_countred > 1:
            summary_countered[total_countred-2][1].append(
                str(list(Counter(bad_against).keys())[i]))

    result = []
    for i in reversed(summary_countered):
        result.append({
            'total_countered': i[0]+1,
            'heros': [i.replace(" ", "_") for i in i[1]]
        })

    return result


def __summary_attack_abilities__(heros, df=DATA_HERO):
    attack_type = []
    attack_demage = []
    summary_attack = []
    summary_demage = []

    df = df.loc[df['Hero'].isin(heros)]

    for row in df['Abilities attack type']:
        str1 = row.replace(']', '').replace('[', '')
        str1 = str1.replace(" '", "").replace("'", "")
        for i in str1.replace('"', '').split(","):
            if i != "":
                attack_type.append(i)

    for row in df['Abilities attack demage']:
        str1 = row.replace(']', '').replace('[', '')
        str1 = str1.replace(" '", "").replace("'", "").replace(" I", "I")
        for i in str1.replace('"', '').split(","):
            if i != "":
                attack_demage.append(i)

    summary_attack = [
        list(Counter(attack_type).keys()),
        list(Counter(attack_type).values())
        ]

    summary_demage = [
        list(Counter(attack_demage).keys()),
        list(Counter(attack_demage).values())
        ]

    return summary_attack, summary_demage


def set_up():
    USER_DATA_DRAFTING = read_user_data()

    radiant = USER_DATA_DRAFTING['radiant']
    dire = USER_DATA_DRAFTING['dire']

    radiant_data, dire_data = __hero__(radiant, dire)

    s_r_attack, s_r_armor, s_r_speed = __summary_atribute__(radiant_data)
    s_r_attack_type, s_r_demage_type = __summary_attack_abilities__(radiant)
    s_r_countered = __summary_countered__(radiant)

    s_d_attack, s_d_armor, s_d_speed = __summary_atribute__(dire_data)
    s_d_attack_type, s_d_demage_type = __summary_attack_abilities__(dire)
    s_d_countered = __summary_countered__(dire)

    arr_show_hero_info = USER_DATA_DRAFTING['arr_show_hero_info']
    radiant_data, dire_data = __setup_show_ui_hero_info(
                                    radiant_data,
                                    dire_data,
                                    arr_show_hero_info)

    stats = __setup_show_ui_stat__(
                id_show=USER_DATA_DRAFTING['statistics']['id_show'])

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
                'settings':
                    USER_DATA_DRAFTING['summary']['radiant']['settings']
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
                'settings': USER_DATA_DRAFTING['summary']['dire']['settings']
            }
        ]
    }

    return propt

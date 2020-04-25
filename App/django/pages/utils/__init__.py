import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data_hero = pd.read_csv(BASE + "/../../static/csv/hero.csv")
data_stat_win_rate = pd.read_csv(
    BASE + "/../../static/csv/hero_win_top5.csv")
data_stat_most_played = pd.read_csv(
    BASE + "/../../static/csv/hero_most_played_top5.csv")
data_stat_meta = pd.read_csv(
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
                'index': index
            })

        index += 1

    return data, index


def hero(radiant, dire, df=data_hero):
    index = 0

    radiant_data, index = __get_hero_data__(radiant, df, index)
    dire_data, index = __get_hero_data__(dire, df, index)

    return radiant_data, dire_data


def stat_meta(meta_id, df=data_stat_meta):
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
            'name': row[0].replace(" ","_"),
            'win_rate': __rounding__(row[1]),
            'pick_rate': __rounding__(row[2])
            })

    result = {
        'id': _id,
        'title': _title,
        'heros': heros
        }

    return result


def stat_win_rate(df=data_stat_win_rate):
    _id = "hero_win_rate"
    _title = "Top 5 Heros base on win rate"

    heros = []
    for index, row in df.iterrows():
        heros.append({
            'name': row['Hero'].replace(" ","_"),
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


def stat_most_played(df=data_stat_most_played):
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

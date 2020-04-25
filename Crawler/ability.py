#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:58:55 2020
counters
@author: baltschun
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib
import os

BASE = (os.path.dirname(os.path.realpath(__file__)))

def __heros_ability__(name):
    print(name)
    url = "https://dota2.gamepedia.com/{}".format(name)
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    
    abilities = soup.find_all("div", {"class": "ability-background"})
    abilities_info = [name]
    for ab in abilities:
        skill = ab.find_all("div", {"style": "display: inline-block; width: 32%; vertical-align: top;"})
        
        ability = skill[0].find("a").text
        affects = skill[1].text.replace("Affects","")
        
        demage = []
        try:
            demages = skill[2].find_all("a")
            for d in demages:
                demage.append(d.text)
        except Exception:
            pass
        abilities_info.append([ability, affects, demage])
        
    return abilities_info 
    
def __get_heros_name__():
    url = "https://dota2.gamepedia.com/Dota_2_Wiki"
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    
    heros = soup.find_all("div", {"class": "heroentrytext"})
    heros_name = []
    for h in heros:
        heros_name.append(h.text)
    
    return heros_name


def __download_heros_abilities_attack_info__():
    heros_name = __get_heros_name__()
    abilities = [__heros_ability__(hero) for hero in heros_name]
    abbs = []
    for hero in abilities:
        hero_abilities = []
        hero_demage = []
        for skill in hero[1:]:
            if skill[2] != []:
                try:
                    affects = skill[1].split("  / ").index("Enemies")
                    if len(skill[2]) > 1:
                        hero_abilities.append(skill[0])
                        hero_demage.append(skill[2][affects])
                    else:
                        hero_abilities.append(skill[0])
                        hero_demage.append(skill[2][0])
                except Exception:
                    pass
        abbs.append([hero[0], hero_abilities, hero_demage])
        df = pd.DataFrame(abbs, columns=['Hero', 'Abilities attack type', 'Abilities attack demage'])
        df.to_csv(BASE +"/hero_abilities.csv", index=False)

__download_heros_abilities_attack_info__()


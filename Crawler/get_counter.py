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

def __heros_counter__(name):
    print(name)
    url = "https://dota2.gamepedia.com/{}/Counters".format(name)
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    
    content = soup.find("div", {"id": "bodyContent"})
    content = content.find("div", {"id": "mw-content-text"})
    heros = content.find_all(["b","h2"])
    
    result = [[],[],[]]
    target = 0
    for h in heros:
        value = h.text.replace("...[edit]","").replace("...","")
        if value != "" and value != "Contents":
            if value == "Bad against":
                target = 0
                continue
            if value == "Good against":
                target = 1
                continue
            if value == "Works well with":
                target = 2
                continue
            result[target].append(value)
    
    return name, result[0], result[1], result[2]
    
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

def __download_heros_counters__():
    heros_name = __get_heros_name__()
    counters = [__heros_counter__(hero) for hero in heros_name]
    
    df = pd.DataFrame(counters, columns=['Hero', 'Bad against', 'Good against', 'Works well with'])
    df.to_csv(BASE +"/hero_counters.csv", index=False)


__download_heros_counters__()

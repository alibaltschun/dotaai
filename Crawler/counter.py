#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:58:55 2020

@author: baltschun
"""

from bs4 import BeautifulSoup
import requests

def __heros_counter__(name):
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
        value = h.text.replace("...[edit]","")
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
    
    return result


heros_counter = __heros_counter__("Zeus")
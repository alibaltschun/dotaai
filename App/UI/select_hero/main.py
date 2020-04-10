# -*- coding: utf-8 -*-

import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../../assets/csv/hero.csv")

def __hero_icon__(hero_name):
    ui = """
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/{}_minimap_icon.png"><img></a></li>""".format(hero_name)
    return ui

def __hero_icon_ui__(heros):
    str1 = heros.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" ","_")
    heros_name = str1.replace('"','').split(",")
    
    ui = ""
    for hero_name in heros_name:
        ui += __hero_icon__(hero_name)
    return ui

def __hero__(hero_name, index, data=data):
    hero_data = data.loc[data['Hero'] == hero_name]
    
    ui = """
                <div class="d-flex flex-column" style="max-width: 300px;">
                    <button class="text-uppercase mt-2 font-weight-bold btn grey lighten-5 custom-no-shadows font-weight-bold indigo-text" data-toggle="collapse" data-target="#collapseExample{}">
                        {}
                    </button>
    
                    <div class="collapse pl-2 pr-2 " id="collapseExample{}" >
                        <div class="media grey lighten-3 rounded m-0">
                            <i class="fas fa-user-cog pl-2 pt-2 pr-1 grey-text"></i>
                            <div class="media-body ">
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Hero Attribute">
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_strength.png">{}<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_agility.png">{}<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_intelligence.png">{}<img></a></li>
                                    <br>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/attack.png"></li>{}-{}<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/defend.png">{}<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/movement.png">{}<img></a></li>
                                </div>
                            </div>
                        </div>
    
                        <div class="media teal lighten-5 rounded mt-1">
                            <i class="fas fa-user-friends pl-2 pt-2 pr-1 green-text"></i>
                            <div class="media-body" >
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Works well with">
                                    {}
                                </div>
                            </div>
                        </div>
                        
                        <div class="media blue lighten-5 rounded mt-1">
                            <i class="fas fa-laugh pl-2 pt-2 pr-1 blue-text"></i>
                            <div class="media-body">
                                <div class="container mb-1 mt-1 text-center " style="width: 100%;" data-toggle="tooltip" data-placement="left" title="Good against">
                                    {}
                                </div>
                            </div>
                        </div>
    
                        <div class="media red lighten-5 rounded mt-1">
                            <i class="fas fa-skull-crossbones pl-2 pt-2 pr-1 red-text"></i>
                            <div class="media-body" >
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Bad against">
                                   {}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            
            
            
    """.format(
        index,
        hero_name,
        index,
        int(hero_data['STR']),
        int(hero_data['AGI']),
        int(hero_data['INT']),
        int(hero_data['DMG (MIN)']),
        int(hero_data['DMG (MAX)']),
        int(hero_data['AR']),
        int(hero_data['MS']),
        __hero_icon_ui__(hero_data['Works well with'].item()),
        __hero_icon_ui__(hero_data['Good against'].item()),
        __hero_icon_ui__(hero_data['Bad against'].item()),
        )
    return ui


def generate_ui():
    radiant = ["Io", "Lina", "Lion", "Zeus", "Omniknight"]
    dire = ["Sven", "Tusk", "Bloodseeker", "Medusa", "Timbersaw"]
    
    ui_radiant = [__hero__(radiant[i],i) for i in range(5)]
    ui_dire = [__hero__(dire[i],i+5) for i in range(5)]
    
    with open(BASE + "/top.html","r") as file:
        top=file.read()
    
    with open(BASE + "/bottom.html","r") as file:
        bottom=file.read()
    
    with open(BASE + "/index.html","w+") as file:
        file.write(top)
        for u in ui_radiant:
            file.write(u)
        for u in ui_dire:
            file.write(u)
        file.write(bottom)

generate_ui()
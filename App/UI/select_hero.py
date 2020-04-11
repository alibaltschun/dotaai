
import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../assets/csv/hero.csv")

def __hero_icon__(hero_name):
    ui = """
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></a></li>""".format(hero_name)
    return ui

def __hero_icon_ui__(heros):
    str1 = heros.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" ","_")
    heros_name = str1.replace('"','').split(",")
    
    ui = ""
    for hero in heros_name:
        ui += __hero_icon__(hero)
    return ui


def __hero__(hero_name, index, data=data):
    if hero_name != "unselection":
        hero_data = data.loc[data['Hero'] == hero_name]
        
        ui = """
                    <div class="d-flex flex-column" style="max-width: 300px;">
                        <button class="text-uppercase mt-1 font-weight-bold btn blue-grey darken-2 custom-no-shadows font-weight-bold" data-toggle="collapse" data-target="#collapseExample{}">
                            {}
                        </button>
        
                        <div class="collapse pl-2 pr-2 " id="collapseExample{}" >
                            <div class="media blue-grey darken-1 rounded m-0" data-toggle="tooltip" data-placement="left" title="Hero Attribute">
                                <i class="fas fa-user-cog pl-2 pt-2 pr-1grey-text"></i>
                                <div class="media-body ">
                                    <div class="container mb-1 mt-1 text-center grey-text" >
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/icon_strength.png">{}<img></a></li>
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/icon_agility.png">{}<img></a></li>
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/icon_intelligence.png">{}<img></a></li>
                                        <br>
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/attack.png"></li>{}-{}<img></a></li>
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/defend.png">{}<img></a></li>
                                        <li class="list-inline-item pt-1"><a ><img class="icon" src="./../assets/img/attribute/movement.png">{}<img></a></li>
                                    </div>
                                </div>
                            </div>
        
                            <div class="media blue-grey darken-2 rounded mt-1" data-toggle="tooltip" data-placement="left" title="Works well with">
                                <i class="fas fa-user-friends pl-2 pt-2 pr-1 green-text"></i>
                                <div class="media-body" >
                                    <div class="container mb-1 mt-1 text-center" >
                                        {}
                                    </div>
                                </div>
                            </div>
                            
                            <div class="media blue-grey darken-3 rounded mt-1" style="width: 100%;" data-toggle="tooltip" data-placement="left" title="Good against">
                                <i class="fas fa-laugh pl-2 pt-2 pr-1 blue-text"></i>
                                <div class="media-body">
                                    <div class="container mb-1 mt-1 text-center " >
                                        {}
                                    </div>
                                </div>
                            </div>
        
                            <div class="media blue-grey darken-4 rounded mt-1" data-toggle="tooltip" data-placement="left" title="Bad against">
                                <i class="fas fa-skull-crossbones pl-2 pt-2 pr-1 red-text"></i>
                                <div class="media-body" >
                                    <div class="container mb-1 mt-1 text-center" >
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
    else:
        ui = """
                    <div class="d-flex flex-column" style="max-width: 300px;">
                        <button class="text-uppercase mt-1 font-weight-bold btn blue-grey darken-2 custom-no-shadows font-weight-bold" disabled>
                            {}
                        </button>
                    </div>
                
        """.format(hero_name)
        return ui
        
def generate_ui(radiant, dire):   
    ui_radiant = [__hero__(radiant[i].title(),i) for i in range(5)]
    ui_dire = [__hero__(dire[i].title(),i+5) for i in range(5)]
    
    with open(BASE + "/utils/head.html","r") as file:
        head=file.read()

    with open(BASE + "/utils/style_select_hero.html","r") as file:
        style=file.read()
    
    with open(BASE + "/utils/close_head_open_body.html","r") as file:
        head_body=file.read()
    
    with open(BASE + "/utils/js_select_hero.html","r") as file:
        js=file.read()
    
    with open(BASE + "/utils/bottom.html","r") as file:
        bottom=file.read()
    
    

    with open(BASE + "/index.html","w+") as file:
        file.write(head)
        file.write(style)
        file.write(head_body)
        for u in ui_radiant:
            file.write(u)
        file.write("<hr>")
        for u in ui_dire:
            file.write(u)
        file.write(js)
        file.write(bottom)


# generate_ui(["Lion" for i in range(5)], ["Lion" for i in range(5)])
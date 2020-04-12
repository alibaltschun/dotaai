
import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../assets/csv/hero.csv")
data_stat_win_rate = pd.read_csv(BASE + "/../assets/csv/hero_win_top5.csv")
data_stat_most_played = pd.read_csv(BASE + "/../assets/csv/hero_most_played_top5.csv")
data_stat_meta = pd.read_csv(BASE + "/../assets/csv/hero_meta.csv")

def __hero_icon__(hero_name):
    ui = """
                                        <li class="list-inline-item "><a href="#" ><img class="icon" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></a></li>""".format(hero_name)
    return ui

def __input_hero_statistics_win_rate__(name, win_rate, pick_rate, kda_ratio):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-5"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}</td>
                        </tr> 
        """.format(name.replace(" ","_"), win_rate, pick_rate, kda_ratio)
    return ui


def __input_hero_statistics_most_played__(name, matches_played, win_rate, pick_rate, kda_ratio):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-5"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}</td>
                        </tr> 
        """.format(name.replace(" ","_"), matches_played, win_rate, pick_rate, kda_ratio)
    return ui


def __input_hero_statistics_meta__(name, pick, win):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-5"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                        </tr>  
        """.format(name.replace(" ","_"), pick, win)
    return ui
    

def __ui_statistics_win_rate__():
    top = """
            <!-- hero statistics -->
            <div class="gallery" id="gallery" 
                style="position: absolute;
                margin-left: auto;
                margin-right: auto;
                left: 0;
                right: 0;
                padding-right: 400px;
                width: 900px;"
                >

                <div class="animation hero_win_rate card card-list mb-4 blue-grey darken-1" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0"><i class="fas fa-inbox pr-2"></i>Top 5 Heros base on win rate - This week</p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class=" filter" data-rel="close"><i class="fas fa-times"></i></a></p>
                        </div>
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2 pl-5" scope="col">Hero</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Win Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Pick Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">KDA Ratio</th>
                            </tr>
                        </thead>
                        <tbody>
                    """
    bot = """               </tbody>
                    </table>
                </div>
            </div>"""

    ui = ""
    for _, row in data_stat_win_rate.iterrows():
        ui += __input_hero_statistics_win_rate__(row['Hero'], row['Win Rate'], row['Pick Rate'], row['KDA Ratio'])
    return top + ui + bot




def __ui_statistics_most_played__():
    top = """
            <!-- hero statistics -->
            <div class="gallery" id="gallery" 
                style="position: absolute;
                margin-left: auto;
                margin-right: auto;
                left: 0;
                right: 0;
                padding-right: 400px;
                width: 900px;"
                >

                <div class="animation hero_most_played card card-list mb-4 blue-grey darken-1" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0"><i class="fas fa-inbox pr-2"></i>Top 5 Heros base on most played - This week</p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class=" filter" data-rel="close"><i class="fas fa-times"></i></a></p>
                        </div>
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2 pl-5" scope="col">Hero</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Matches Played</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Win Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Pick Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">KDA Ratio</th>
                            </tr>
                        </thead>
                        <tbody>
                    """
    bot = """               </tbody>
                    </table>
                </div>
            </div>"""

    ui = ""
    for _, row in data_stat_most_played.iterrows():
        ui += __input_hero_statistics_most_played__(row['Hero'],row['Matches Played'], row['Win Rate'], row['Pick Rate'], row['KDA Ratio'])
    return top + ui + bot


def __ui_statistics_meta__(meta_id, df=data_stat_meta):
    top = """
            <div class="gallery" id="gallery" 
                style="position: absolute;
                margin-left: auto;
                margin-right: auto;
                left: 0;
                right: 0;
                padding-right: 400px;
                width: 900px;"
                >

                <div class="animation hero_meta_{} card card-list mb-4 blue-grey darken-1 z-depth-2" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-lg-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0"><img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png"> - Top 5 Heros base on meta </p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class=" filter" data-rel="close"><i class="fas fa-times"></i></a></p>
                            
                        </div>
                        
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2 pl-5" scope="col">Hero</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Pick Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Win Rate</th>
                            </tr>
                        </thead>
                        <tbody>
                        """.format(meta_id)
    bot = """
                        </tbody>
                    </table>
                </div>
            </div>
            """

    ui = ""
    df_meta = df.sort_values(('rank {} win'.format(meta_id)), ascending=False)[:5]
    for _, row in df_meta.iterrows():
        ui += __input_hero_statistics_meta__(
            row['Hero'],
            row['rank {} pick'.format(meta_id)],
            row['rank {} win'.format(meta_id)]
            )
    return top + ui + bot


def __ui_statistics__():
    top = """
    <footer class="fixed-bottom">
        <div class="d-flex align-items-end">
        """
    bot = """
        <div class="dark-grey-text d-flex justify-content-center"
             style="position: absolute;
                    right: 1000px;
                    ">

            <div class="d-flex flex-column justify-content-center mr-5 mb-3 p-1 pb-2" >
                <button class=" font-weight-bold btn  mdb-color lighten-3 custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_123" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Herald.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Guardian.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Crusader.png">
                </button>
                <button class=" font-weight-bold btn  mdb-color lighten-3 custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_4" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Archon.png">
                </button>
                <button class=" font-weight-bold btn  mdb-color lighten-3 custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_5" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Legend.png">
                </button>
                <button class=" font-weight-bold btn  mdb-color lighten-3 custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_6" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png">
                </button>
                <button class=" font-weight-bold btn  mdb-color lighten-3 custom-no-shadows font-weight-bold filter  mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_78" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Divine.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png">
                </button>
                <button class="font-weight-bold btn  mdb-color lighten-3  custom-no-shadows font-weight-bold filter mb-0 pt-2 pb-2" data-rel="hero_win_rate" style="width: 150px;">
                    Win Rate
                </button>
                <button class="font-weight-bold btn  mdb-color lighten-3  custom-no-shadows font-weight-bold filter mb-0 pt-2 pb-2" data-rel="hero_most_played" style="width: 150px;">
                    Most Played
                </button>
            </div>
        </div>
    </div>
</footer>"""
    data = (
        __ui_statistics_win_rate__() +
        __ui_statistics_most_played__() +
        __ui_statistics_meta__('123') +
        __ui_statistics_meta__('4') +
        __ui_statistics_meta__('5') +
        __ui_statistics_meta__('6') +
        __ui_statistics_meta__('78'))
    return top + data + bot

def __hero_icon_ui_counter__(heros):
    str1 = heros.replace(']','').replace('[','').replace(" '","").replace("'","").replace(" ","_")
    heros_name = str1.replace('"','').split(",")
    
    ui = ""
    for hero in heros_name:
        ui += __hero_icon__(hero)
    return ui


def __input_hero_counter__(hero_name, index, data=data):
    if hero_name != "unselection":
        hero_data = data.loc[data['Hero'] == hero_name]
        
        ui = """
                    <div class="d-flex flex-column" style="max-width: 122px;">
                        <button class="btn-sm mt-2 font-weight-bold btn blue-grey darken-3 custom-no-shadows font-weight-bold" data-toggle="collapse" data-target="#collapseExample{}">
                            {}
                        </button>
        
                        <div class="collapse pl-1 pr-1 " id="collapseExample{}" >
                            
                            <div class="media blue-grey darken-1 rounded m-0" data-toggle="tooltip" data-placement="left" title="Hero Attribute">
                                <div class="media-body d-flex flex-row justify-content-center pb-1 grey-text2" >
                                    <div class="d-flex flex-column align-items-start" >
                                        <li class="list-inline-item pt-1 pl-2"><a><img class="icon" src="./../assets/img/attribute/icon_strength.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1 pl-2"><a><img class="icon" src="./../assets/img/attribute/icon_agility.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1 pl-2"><a><img class="icon" src="./../assets/img/attribute/icon_intelligence.png"><small> {}</small><img></a></li>
                                    </div>
                                    <div class="d-flex flex-column align-items-start" >
                                        <li class="list-inline-item pt-1"><a><img class="icon" src="./../assets/img/attribute/attack.png"><small> {}-{}</small><img></a></li>
                                        <li class="list-inline-item pt-1"><a><img class="icon" src="./../assets/img/attribute/defend.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1"><a><img class="icon" src="./../assets/img/attribute/movement.png"><small> {}</small><img></a></li>
                                    </div>
                                </div>
                            </div>
        
                            <div class="media blue-grey darken-2 rounded mt-1" data-toggle="tooltip" data-placement="left" title="Works well with">
                                <i class="fas fa-user-friends pl-2 pt-2 pr-1 green-text"></i>
                                <div class="media-body" >
                                    <div class="mb-1 mt-1 ml-2">
                                        {}
                                    </div>
                                </div>
                            </div>
                            
                            <div class="media blue-grey darken-3 rounded mt-1" style="width: 100%;" data-toggle="tooltip" data-placement="left" title="Good against">
                                <i class="fas fa-laugh pl-2 pt-2 pr-1 blue-text"></i>
                                <div class="media-body">
                                    <div class="mb-1 mt-1 ml-2" >
                                        {}
                                    </div>
                                </div>
                            </div>
        
                            <div class="media blue-grey darken-4 rounded mt-1" data-toggle="tooltip" data-placement="left" title="Bad against">
                                <i class="fas fa-skull-crossbones pl-2 pt-2 pr-1 red-text"></i>
                                <div class="media-body" >
                                    <div class="mb-1 mt-1 ml-2" >
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
            __hero_icon_ui_counter__(hero_data['Works well with'].item()),
            __hero_icon_ui_counter__(hero_data['Good against'].item()),
            __hero_icon_ui_counter__(hero_data['Bad against'].item()),
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
    ui_radiant = [__input_hero_counter__(radiant[i].title(),i) for i in range(5)]
    ui_dire = [__input_hero_counter__(dire[i].title(),i+5) for i in range(5)]
    
    with open(BASE + "/utils/head.html","r") as file:
        head=file.read()

    with open(BASE + "/utils/style_select_hero.html","r") as file:
        style=file.read()
    
    with open(BASE + "/utils/close_head_open_body.html","r") as file:
        head_body=file.read()
    
    with open(BASE + "/utils/flex_select_hero_open.html","r") as file:
        flex_open=file.read()
    
    with open(BASE + "/utils/flex_select_hero_close.html","r") as file:
        flex_close=file.read()
    
    # with open(BASE + "/utils/footer_select_hero.html","r") as file:
        # footer=file.read()
    
    with open(BASE + "/utils/js.html","r") as file:
        js=file.read()
    
    with open(BASE + "/utils/js_select_hero.html","r") as file:
        js_custom=file.read()
    
    with open(BASE + "/utils/bottom.html","r") as file:
        bottom=file.read()
    
    

    with open(BASE + "/index.html","w+") as file:
        file.write(head)
        file.write(style)
        file.write(head_body)
        file.write(flex_open)
        for u in ui_radiant:
            file.write(u)
        file.write("<hr><hr>")
        for u in ui_dire:
            file.write(u)
        file.write(flex_close)
        file.write(__ui_statistics__())
        file.write(js)
        file.write(js_custom)
        file.write(bottom)


radiant = ['Bristleback','Sniper','Lion','Warlock','Pudge']
dire= ['Axe','Bloodseeker','Razor','Zeus','Necrophos']
generate_ui(radiant, dire)
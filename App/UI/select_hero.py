
import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

# data = pd.read_csv(BASE + "/../assets/csv/hero.csv")
data_stat_win_rate = pd.read_csv(BASE + "/../assets/csv/hero_win_top5.csv")
data_stat_most_played = pd.read_csv(BASE + "/../assets/csv/hero_most_played_top5.csv")
data_stat_meta = pd.read_csv(BASE + "/../assets/csv/hero_meta.csv")


def __emblem_icon__(emblem_id):
    if emblem_id == "123":
        return  """
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Herald.png">
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Guardian.png">
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Crusader.png">
        """
    if emblem_id == "4":
        return  """
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Archon.png">
        """
    if emblem_id == "5":
        return  """
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Legend.png">
        """
    if emblem_id == "6":
        return  """
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png">
        """
    if emblem_id == "78":
        return  """
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Divine.png">
                                <img class="icon " style="width: 24px;" src="./../assets/img/emblem/Emoticon_Ranked_Immortal.png">
        """
    return ""
   

def __input_hero_statistics_win_rate__(name, win_rate, pick_rate, kda_ratio):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-3"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}</td>
                        </tr> 
        """.format(
            name.replace(" ","_"),
            str(round(float(win_rate), 2)),
            str(round(float(pick_rate), 2)),
            str(round(float(kda_ratio), 2))
            )
    return ui


def __input_hero_statistics_most_played__(name, matches_played, win_rate, pick_rate, kda_ratio):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-3"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}</td>
                        </tr> 
        """.format(
            name.replace(" ","_"),
            str(round(float(matches_played), 2)),
            str(round(float(win_rate), 2)),
            str(round(float(pick_rate), 2)),
            str(round(float(kda_ratio), 2)),
            )
    return ui


def __input_hero_statistics_meta__(name, pick_rate, win_rate):
    ui = """
                        <tr> 
                            <td class="pt-0 pb-0 pl-3"><img class="icon" style="width: 18px;" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></td>
                            <td class="pt-0 pb-0 ">{}%</td>
                            <td class="pt-0 pb-0 ">{}%</td>
                        </tr>  
        """.format(
            name.replace(" ", "_"),
             str(round(float(pick_rate), 2)),
             str(round(float(win_rate), 2)),
             )
    return ui
    

def __ui_statistics_win_rate__():
    top = """
            <!-- hero statistics -->
            <div class="gallery" id="gallery"
                >

                <div class="animation hero_win_rate card card-list mb-4 blue-grey darken-1" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0"></i>Top 5 Heros base on win rate - <small>This week</small></p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class=" filter pl-3" data-rel="close"><i class="fas fa-times"></i></a></p>
                        </div>
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Hero</th>
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
                >

                <div class="animation hero_most_played card card-list mb-4 blue-grey darken-1" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0"></i>Top 5 Heros base on most played - <small>This week</small></p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class="filter pl-3" data-rel="close"><i class="fas fa-times"></i></a></p>
                        </div>
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Hero</th>
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
                >

                <div class="animation hero_meta_{} card card-list mb-4 blue-grey darken-1" data-toggle="modal"  data-target="#basicExampleModal" style="display: none;">
                    <table class="table table-borderless">
                        <div class="p-2 pr-3 pl-3 d-flex justify-content-lg-between align-items-center blue-grey darken-2">
                            <p class="h5-responsive font-weight-bold mb-0">{} Top 5 Heros base on meta </p>
                            <p class="h5-responsive font-weight-bold mb-0"><a class=" filter pl-3" data-rel="close"><i class="fas fa-times"></i></a></p>
                            
                        </div>
                        
                        <thead> 
                            <tr>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Hero</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Pick Rate</th>
                                <th class="font-weight-bold pb-1 pt-2" scope="col">Win Rate</th>
                            </tr>
                        </thead>
                        <tbody>
                        """.format(meta_id,__emblem_icon__(meta_id))
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
        <div class="container d-flex align-items-end justify-content-md-end" style="width: 600px;">
        """
    bot = """
        <div class="dark-grey-text d-flex justify-content-center"
             style="margin-right: 370PX;"
                    >

            <div class="d-flex flex-column justify-content-center mr-5 mb-3 p-1 pb-2" >
                <button class=" font-weight-bold btn  blue-grey darken-3 text-default custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_123" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Herald.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Guardian.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Crusader.png">
                </button>
                <button class=" font-weight-bold btn  blue-grey darken-3 text-default custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_4" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Archon.png">
                </button>
                <button class=" font-weight-bold btn  blue-grey darken-3 text-default custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_5" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Legend.png">
                </button>
                <button class=" font-weight-bold btn  blue-grey darken-3 text-default custom-no-shadows font-weight-bold filter mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_6" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png">
                </button>
                <button class=" font-weight-bold btn  blue-grey darken-3 text-default custom-no-shadows font-weight-bold filter  mb-0 pt-0 pb-0 pl-4" data-rel="hero_meta_78" style="width: 150px;">
                    Meta - <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Divine.png">
                    <img class="icon " style="width: 18px;" src="./../assets/img/emblem/Emoticon_Ranked_Ancient.png">
                </button>
                <button class="font-weight-bold btn  blue-grey darken-3 text-default  custom-no-shadows font-weight-bold filter mb-0 pt-2 pb-2" data-rel="hero_win_rate" style="width: 150px;">
                    Win Rate
                </button>
                <button class="font-weight-bold btn  blue-grey darken-3 text-default  custom-no-shadows font-weight-bold filter mb-0 pt-2 pb-2" data-rel="hero_most_played" style="width: 150px;">
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

from html.select_hero.header import input_hero_counter

def generate_ui(radiant, dire):
    ui_radiant = [input_hero_counter(radiant[i], i) for i in range(5)]
    ui_dire = [input_hero_counter(dire[i], i+5) for i in range(5)]

    with open(BASE + "/utils/head.html", "r") as file:
        head = file.read()

    with open(BASE + "/utils/style_select_hero.html", "r") as file:
        style = file.read()

    with open(BASE + "/utils/close_head_open_body.html", "r") as file:
        head_body = file.read()

    with open(BASE + "/utils/flex_select_hero_open.html", "r") as file:
        flex_open = file.read()

    with open(BASE + "/utils/flex_select_hero_close.html", "r") as file:
        flex_close = file.read()

    with open(BASE + "/utils/js.html", "r") as file:
        js = file.read()

    with open(BASE + "/utils/js_select_hero.html", "r") as file:
        js_custom = file.read()

    with open(BASE + "/utils/bottom.html", "r") as file:
        bottom = file.read()

    with open(BASE + "/index.html", "w+") as file:
        file.write(head)
        file.write(style)
        file.write(head_body)
        file.write(flex_open)
        for u in ui_radiant:
            file.write(u)
        file.write("""<div class="container" style="width: 16vh;"></div>""")
        for u in ui_dire:
            file.write(u)
        file.write(flex_close)
        file.write(__ui_statistics__())
        file.write(js)
        file.write(js_custom)
        file.write(bottom)


# radiant = ['Bristleback', 'Sniper', 'Lion', 'Warlock', 'Pudge']
# dire = ['Axe', 'Bloodseeker', 'Razor', 'Zeus', 'Necrophos']
# generate_ui(radiant, dire)

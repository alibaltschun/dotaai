
import os
import pandas as pd
BASE = (os.path.dirname(os.path.realpath(__file__)))

data = pd.read_csv(BASE + "/../../../assets/csv/hero.csv")


def __hero_icon__(hero_name):
    ui = """
                                        <li class="list-inline-item "><a href="#" ><img class="icon" src="./../assets/img/hero_icon/{}_minimap_icon.png"><img></a></li>""".format(hero_name)
    return ui


def __ui_hero_icon__(heros):
    str1 = heros.replace(']', '').replace('[', '').replace(" '", "")
    str1 = str1.replace("'", "").replace(" ", "_")
    heros_name = str1.replace('"', '').split(",")

    ui = ""
    for hero in heros_name:
        ui += __hero_icon__(hero)
    return ui


def input_hero_counter(hero_name, index, data=data):
    print(hero_name)
    if hero_name.lower() != "unselection":
        hero_data = data.loc[data['Hero'] == hero_name]

        ui = """
                    <div class="d-flex flex-column" style="max-width: 122px;">
                        <button class="btn-sm mt-2 pl-0 pr-0 text-center font-weight-bold btn blue-grey darken-3 text-default custom-no-shadows font-weight-bold" data-toggle="collapse" data-target="#collapseExample{}">
                            {}
                        </button>

                        <div class="collapse pl-1 pr-1 " id="collapseExample{}" >

                            <div class="media blue-grey darken-1 m-0" data-toggle="tooltip" data-placement="left" title="Hero Attribute">
                                <div class="media-body d-flex flex-row justify-content-center pb-1 grey-text2" >
                                    <div class="d-flex flex-column align-items-start" >
                                        <li class="list-inline-item pt-1 pl-2 text-default"><a ><img class="icon" src="./../assets/img/attribute/icon_strength.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1 pl-2 text-default"><a><img class="icon" src="./../assets/img/attribute/icon_agility.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1 pl-2 text-default"><a><img class="icon" src="./../assets/img/attribute/icon_intelligence.png"><small> {}</small><img></a></li>
                                    </div>
                                    <div class="d-flex flex-column align-items-start" >
                                        <li class="list-inline-item pt-1 text-default"><a><img class="icon" src="./../assets/img/attribute/attack.png"><small> {}-{}</small><img></a></li>
                                        <li class="list-inline-item pt-1 text-default"><a><img class="icon" src="./../assets/img/attribute/defend.png"><small> {}</small><img></a></li>
                                        <li class="list-inline-item pt-1 text-default"><a><img class="icon" src="./../assets/img/attribute/movement.png"><small> {}</small><img></a></li>
                                    </div>
                                </div>
                            </div>

                            <div class="media blue-grey darken-2   mt-1" data-toggle="tooltip" data-placement="left" title="Works well with">
                                <i class="fas fa-user-friends pl-2 pt-2 pr-1 green-text"></i>
                                <div class="media-body" >
                                    <div class="mb-1 mt-1 ml-2">
                                        {}
                                    </div>
                                </div>
                            </div>

                            <div class="media blue-grey darken-3   mt-1" style="width: 100%;" data-toggle="tooltip" data-placement="left" title="Good against">
                                <i class="fas fa-laugh pl-2 pt-2 pr-1 blue-text"></i>
                                <div class="media-body">
                                    <div class="mb-1 mt-1 ml-2" >
                                        {}
                                    </div>
                                </div>
                            </div>

                            <div class="media blue-grey darken-4   mt-1" data-toggle="tooltip" data-placement="left" title="Bad against">
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
            __ui_hero_icon__(hero_data['Works well with'].item()),
            __ui_hero_icon__(hero_data['Good against'].item()),
            __ui_hero_icon__(hero_data['Bad against'].item()),
            )
        return ui
    else:
        ui = """
                    <div class="d-flex flex-column" style="max-width: 300px;">
                        <button class="
                                    text-uppercase mt-1
                                    font-weight-bold
                                    btn blue-greydarken-2
                                    custom-no-shadows
                                    font-weight-bold
                                    invisible
                            ">
                            {}
                        </button>
                    </div>

        """.format(hero_name)
        return ui

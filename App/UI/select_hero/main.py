# -*- coding: utf-8 -*-

def __hero__(hero_name):
    ui = """
                <div class="d-flex flex-column" style="max-width: 300px;">
                    <button class="text-uppercase mt-2 font-weight-bold btn grey lighten-5 custom-no-shadows font-weight-bold indigo-text" data-toggle="collapse" data-target="#collapseExample">
                        {}
                    </button>
    
                    <div class="collapse pl-2 pr-2 " id="collapseExample" >
                        <div class="media grey lighten-3 rounded m-0">
                            <i class="fas fa-user-cog pl-2 pt-2 pr-1 grey-text"></i>
                            <div class="media-body ">
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Hero Attribute">
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_strength.png">7<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_agility.png">8<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/icon_intelligence.png">5<img></a></li>
                                    <br>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/attack.png"></li>55-58<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/defend.png">5<img></a></li>
                                    <li class="list-inline-item pt-1"><a ><img class="icon" src="./../../assets/img/attribute/movement.png">395<img></a></li>
                                </div>
                            </div>
                        </div>
    
                        <div class="media teal lighten-5 rounded mt-1">
                            <i class="fas fa-user-friends pl-2 pt-2 pr-1 green-text"></i>
                            <div class="media-body" >
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Works well with">
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Bane_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Batrider_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Beastmaster_minimap_icon.png"><img></a></li>
                                </div>
                            </div>
                        </div>
                        
                        <div class="media blue lighten-5 rounded mt-1">
                            <i class="fas fa-laugh pl-2 pt-2 pr-1 blue-text"></i>
                            <div class="media-body">
                                <div class="container mb-1 mt-1 text-center " style="width: 100%;" data-toggle="tooltip" data-placement="left" title="Good against">
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Abaddon_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Alchemist_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Ancient_Apparition_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Anti-Mage_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Arc_Warden_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Axe_minimap_icon.png"><img></a></li>
                                </div>
                            </div>
                        </div>
    
                        <div class="media red lighten-5 rounded mt-1">
                            <i class="fas fa-skull-crossbones pl-2 pt-2 pr-1 red-text"></i>
                            <div class="media-body" >
                                <div class="container mb-1 mt-1 text-center" data-toggle="tooltip" data-placement="left" title="Bad against">
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Bane_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Batrider_minimap_icon.png"><img></a></li>
                                    <li class="list-inline-item "><a href="#" ><img class="icon" src="./../../assets/img/hero_icon/Beastmaster_minimap_icon.png"><img></a></li>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            
            
            
    """.format(hero_name)
    
    with open("./top.html","r") as file:
        top=file.read()

    with open("./bottom.html","r") as file:
        bottom=file.read()
    
    with open("./index.html","w+") as file:
        file.write(top + ui * 10 + bottom)

    
from .features.timer import check_timer, update_ui
from .features.select_hero import main_select_hero
from .utils.mp3_player import play
from .utils.screen import get_screen_information
from .UI.gameplay import generate_ui
from .UI.main import plot
from .local_server.main import app as server
import os
import time

BASE = (os.path.dirname(os.path.realpath(__file__)))


def __local_server__():
    server.run()


def __ui__():
    generate_ui("instagram : dota2.gg.ai")
    plot()

def __gameplay__(screen_width, screen_height):
    start_asistent = True
    last_minutes = 2
    last_timer = "0:0"
    while True:
        start_asistent, last_minutes, last_timer = check_timer(
                                        screen_width, screen_height,
                                        start_asistent=start_asistent,
                                        last_minutes=last_minutes,
                                        last_timer=last_timer)
                                        
        time.sleep(0.65)


def __select_hero__(screen_width, screen_height):
    file_html_update = BASE + "/temp/html_update.txt"

    heros = [None,None]
    while True:
        radiant, dire = main_select_hero(screen_width, screen_height)
        if heros != [radiant, dire]:
            update_ui()
            heros = [radiant, dire]

        time.sleep(1)

def create_app(menu):
    screen_width, screen_height = get_screen_information()

    if menu == "gameplay":
        __gameplay__(screen_width, screen_height)
    
    if menu == "select_hero":
        __select_hero__(screen_width, screen_height)
    
    if menu == "ui":
        __ui__()
    
    if menu == "server":
        __local_server__()
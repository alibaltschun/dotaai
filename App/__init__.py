from .features.timer import check_timer
from .features.select_hero import main_select_hero
from .utils.mp3_player import play
from .utils.screen import get_screen_information
from .UI.gameplay import generate_ui
from .UI.main import plot
import os
import time

BASE = (os.path.dirname(os.path.realpath(__file__)))


def __ui__():
    generate_ui("")
    plot()

def __gameplay__(screen_width, screen_height):
    start_asistent = True
    last_minutes = 2
    greating = True
    while True:
        start_asistent, last_minutes, greating = check_timer(
                                        screen_width, screen_height,
                                        start_asistent=start_asistent,
                                        last_minutes=last_minutes,
                                        greating=greating)
        time.sleep(0.65)


def __select_hero__(screen_width, screen_height):
    file_html_update = BASE + "/../temp/html_update.txt"

    with open(file_html_update, "w")  as file:
        file.write("1")

    while True:
        main_select_hero(screen_width, screen_height)
        time.sleep(1)

def create_app(menu):
    screen_width, screen_height = get_screen_information()

    if menu == "gameplay":
        __gameplay__(screen_width, screen_height)
    
    if menu == "select_hero":
        __select_hero__(screen_width, screen_height)
    
    if menu == "ui":
        __ui__()
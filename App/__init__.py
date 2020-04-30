from .features.timer import check_timer, update_ui
# from .features.select_hero import main_select_hero
from .features.ui import check_ui
from .utils.screen import get_screen_information
from .UI.gameplay import generate_ui as generate_ui_gameplay
# from .UI.select_hero import generate_ui as generate_ui_drafting
from .UI.main import plot
from .local_server.main import app as server
import os
import time

BASE = (os.path.dirname(os.path.realpath(__file__)))


def __local_server__():
    server.run()


def __ui__():
    generate_ui_gameplay(["instagram : dota2.gg.ai"])
    plot()


def __ui_menu__(screen_width, screen_height):
    generate_ui_gameplay(["instagram : dota2.gg.ai"])
    update_ui()
    _check_ui = 0

    while True:

        time.sleep(1)

        # check ui every n seconds
        _check_ui += 1

        if _check_ui == 3:

            # reset _check)ui
            _check_ui = 0

            # pred ui
            ui = check_ui(screen_width, screen_height)

            if ui != "menu":
                break

    __change_ui__(screen_width, screen_height, ui)


def __change_ui__(screen_width, screen_height, ui=None):

    if ui is None:
        ui = ui = check_ui(screen_width, screen_height)

    print(ui)

    if ui == "gameplay":
        __gameplay__(screen_width, screen_height)
    if ui == "drafting":
        __select_hero__(screen_width, screen_height)
    if ui == "menu":
        __ui_menu__(screen_width, screen_height)


def __gameplay__(screen_width, screen_height):
    start_asistent = True
    last_minutes = 1
    last_timer = "0:0"
    _check_ui = 0
    while True:
        start_asistent, last_minutes, last_timer = check_timer(
                                        screen_width, screen_height,
                                        start_asistent=start_asistent,
                                        last_minutes=last_minutes,
                                        last_timer=last_timer)

        time.sleep(0.65)

        # check ui every n seconds
        _check_ui += 1
        if _check_ui == 3:

            # reset _check)ui
            _check_ui = 0

            # pred ui
            ui = check_ui(screen_width, screen_height)

            if ui != "gameplay":
                break

    __change_ui__(screen_width, screen_height, ui)


def __select_hero__(screen_width, screen_height):

    radiant = ['unselection', 'unselection', 'unselection',
               'unselection', 'unselection']
    dire = ['unselection', 'unselection', 'unselection',
            'unselection', 'unselection']

    # generate_ui_drafting(radiant, dire)
    update_ui()

    heros = [None, None]
    _check_ui = 0
    while True:
        # radiant, dire = main_select_hero(screen_width, screen_height)
        if heros != [radiant, dire]:
            update_ui()
            heros = [radiant, dire]

        time.sleep(1)

        # check ui every n seconds
        _check_ui += 1
        if _check_ui == 3:

            # reset _check)ui
            _check_ui = 0

            # pred ui
            ui = check_ui(screen_width, screen_height)

            if ui != "drafting":
                break

    print("break")
    __change_ui__(screen_width, screen_height, ui)


def create_app(menu):
    screen_width, screen_height = get_screen_information()

    if menu == "ai":
        __change_ui__(screen_width, screen_height)

    if menu == "ui":
        __ui__()

    if menu == "server":
        __local_server__()

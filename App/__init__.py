from .features.timer import check_timer
from .features.drafting import main_drafting, update_drafting_data
from .features.ui import check_ui
from .utils.screen import get_screen_information
from .UI.gameplay import generate_ui as generate_ui_gameplay
from .UI.main import plot
from .local_server.main import app as server
import os
import time
import json

BASE = (os.path.dirname(os.path.realpath(__file__)))


def __read_user_data__():
    USER_DATA_DRAFTING = open(BASE + "/django/local_data/drafting.json")
    USER_DATA_DRAFTING = USER_DATA_DRAFTING.read()
    USER_DATA_DRAFTING = json.loads(USER_DATA_DRAFTING)
    return USER_DATA_DRAFTING


def __save_user_data__(data):
    with open((BASE + "/django/local_data/drafting.json"), 'w') as f:
        json.dump(data, f)


def __update_data_ui__(ui):
    data = __read_user_data__()
    data["have_update"] = 1
    data["ui"] = ui
    __save_user_data__(data)


def __local_server__():
    server.run()


def __ui__():
    generate_ui_gameplay(["instagram : dota2.gg.ai"])
    plot()


def __ui_menu__(screen_width, screen_height):
    generate_ui_gameplay(["instagram : dota2.gg.ai"])
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

    print('ui', ui)

    if ui == "gameplay":
        __update_data_ui__(ui)
        __gameplay__(screen_width, screen_height)
    if ui == "drafting":
        __update_data_ui__(ui)
        __drafting__(screen_width, screen_height)
    # if ui == "menu":
    #     __update_data_ui__(ui)
    #     __ui_menu__(screen_width, screen_height)


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

            # reset _check_ui
            _check_ui = 0

            # pred ui
            ui = check_ui(screen_width, screen_height)

            if ui != "gameplay":
                break

    __change_ui__(screen_width, screen_height, ui)


def __drafting__(screen_width, screen_height):

    radiant = ['unselection', 'unselection', 'unselection',
               'unselection', 'unselection']
    dire = ['unselection', 'unselection', 'unselection',
            'unselection', 'unselection']

    update_drafting_data(radiant, dire)

    heros = [None, None]
    _check_ui = 0
    while True:
        radiant, dire = main_drafting(screen_width, screen_height)
        if heros != [radiant, dire]:
            update_drafting_data(radiant, dire)
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

    __change_ui__(screen_width, screen_height, ui)


def create_app(menu):
    screen_width, screen_height = get_screen_information()

    if menu == "ai":
        __change_ui__(screen_width, screen_height)

    if menu == "ui":
        __ui__()

    if menu == "server":
        __local_server__()

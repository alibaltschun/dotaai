from .features.gameplay_hero import call_heros_on_team
from .features.teleport import check_teleport
from .features.timer import check_timer
from .features.team import pred_team
from .features.select_hero import get_heros_name
from .utils.mp3_player import play
from .utils.screen import get_screen_information

import time


def create_app():
    screen_width, screen_height = get_screen_information()
    call_heros_on_team(screen_width, screen_height)
    # check_teleport(screen_width, screen_height)

    # start_asistent = True
    # last_minutes = 2
    # greating = True
    # while True:
    #     start_asistent, last_minutes, greating = check_timer(
    #                                     screen_width, screen_height,
    #                                     start_asistent=start_asistent,
    #                                     last_minutes=last_minutes,
    #                                     greating=greating)
    #     time.sleep(0.65)

    # pred_team(screen_width, screen_height)
    # get_heros_name(screen_width, screen_height)

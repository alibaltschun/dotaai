from .features.heros_name import call_heros_on_team
from .features.teleport import check_teleport
from .utils.mp3_player import play
from .utils.screen import get_screen_information


def create_app():
    screen_width, screen_height = get_screen_information()
    call_heros_on_team(screen_width, screen_height)
    # check_teleport(screen_width, screen_height)

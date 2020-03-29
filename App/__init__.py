from .features.heros_name import call_heros_on_team
from .utils.mp3_player import play
# from .utils.screen import get_screen_information


def create_app():
    # screen_width, screen_height = get_screen_information()
    screen_width, screen_height = 1080, 1920
    
    radiant_heros, dire_heros = call_heros_on_team(screen_width, screen_height)
    play("lina", voice_type="hero")
    for hero in radiant_heros:
        play(hero.lower(), voice_type="hero")

    for hero in dire_heros:
        play(hero.lower(), voice_type="hero")

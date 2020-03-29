# from PIL import ImageGrab
import pyscreenshot as ImageGrab
from fastai.vision import load_learner, open_image
from ..utils.mp3_player import play

import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/list_hero'
model = load_learner(MODEL_PATH)


def __split_hero_icon__(img):
    w, h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i * w / 5, 0, (i+1) * w / 5, h)))
    return r


def call_heros_on_team(screen_width, screen_height, learn=model, ):

    # calculate const for crop from screenshot
    if screen_width*9 > screen_height*21:
        delta_timer = 0.556
    else:
        delta_timer = 0.556

    # grab radiant heros
    left = ImageGrab.grab(bbox=(
        int(screen_width * 0.28),
        4,
        int(screen_width - screen_width * delta_timer),
        int(screen_height - screen_height * 0.965-3)))

    # grab dire heros
    right = ImageGrab.grab(bbox=(
        int(screen_width * delta_timer),
        4,
        int(screen_width - screen_width * 0.28),
        int(screen_height - screen_height * 0.965-3)))

    # resize img
    left = left.resize((210, 18))
    right = right.resize((210, 18))

    # split all heros from img
    radiant_icon = __split_hero_icon__(left)
    dire_icon = __split_hero_icon__(right)

    # set array for heros name
    radiant_heros = []
    dire_heros = []

    # temp img from model pred
    temp_file = BASE + "/../temp/header_hero.png"

    # get all radiant heros name
    for hero in radiant_icon:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        radiant_heros.append(hero_name)

    # get all dire heros name
    for hero in dire_icon:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        dire_heros.append(hero_name)

    # for hero in radiant_heros:
    #     play(hero.lower(), voice_type="hero")

    # for hero in dire_heros:
    #     play(hero.lower(), voice_type="hero")

    # play("lina", voice_type="hero")

    return radiant_heros, dire_heros

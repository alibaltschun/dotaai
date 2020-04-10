from PIL import ImageGrab
# import pyscreenshot as ImageGrab
from fastai.vision import load_learner, open_image
from ..utils.mp3_player import play_opening_game
import time
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
        delta_timer = 0.54
        wide = 1
        print(1)
    else:
        delta_timer = 0.556
        wide = 0
        print(0)

    print("get image")
    start_time = time.time()

    # grab radiant heros
    left = ImageGrab.grab((
        int(screen_width * 0.28 + wide * screen_width * 0.056),
        4,
        int(screen_width - screen_width * delta_timer),
        int(screen_height - screen_height * 0.965-3)))

    # grab dire heros
    right = ImageGrab.grab((
        int(screen_width * delta_timer),
        4,
        int(screen_width - screen_width * 0.28 - wide * screen_width * 0.056),
        int(screen_height - screen_height * 0.965-3)))

    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    print("resize and split")
    # resize img
    left = left.resize((210, 18))
    right = right.resize((210, 18))

    # split all heros from img
    radiant_icon = __split_hero_icon__(left)
    dire_icon = __split_hero_icon__(right)

    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # set array for heros name
    radiant_heros = []
    dire_heros = []

    # temp img from model pred
    temp_file = BASE + "/../temp/header_hero.png"

    print("predict hero")
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # get all radiant heros name
    for hero in radiant_icon:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        radiant_heros.append(hero_name.lower().replace("_", " "))

    # get all dire heros name
    for hero in dire_icon:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        dire_heros.append(hero_name.lower().replace("_", " "))

    play_opening_game(radiant_heros, dire_heros)
    print("--- %s seconds ---" % (time.time() - start_time))

from PIL import ImageGrab
# import pyscreenshot as ImageGrab

from fastai.vision import load_learner, open_image
import time
import os
from ..UI.select_hero import generate_ui

BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/select_hero'
model = load_learner(MODEL_PATH)


def split(img):
    w,h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i*w/5,0,(i+1)*w/5,h)))
    return r


def main_select_hero(screen_width, screen_height, learn=model, ):
    # calculate const for crop from screenshot
    # print("get image")
    start_time = time.time()

    header = ImageGrab.grab((
        (screen_width*0.205),
        0,
        (screen_width-screen_width*0.205)
        ,screen_height-screen_height*0.93))

    screen_width, screen_height = header.size
    left = header.crop((0,0,screen_width*.413,screen_height))
    right = header.crop((screen_width-screen_width*.413,0,screen_width,screen_height))
        
    radiant = split(left)
    dire = split(right)

    # print("--- %s seconds ---" % (time.time() - start_time))
    # start_time = time.time()

    # set array for heros name
    radiant_heros = []
    dire_heros = []

    # temp img from model pred
    temp_file = BASE + "/../temp/select_hero.png"

    # print("predict hero")
    # print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # get all radiant heros name
    for hero in radiant:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        radiant_heros.append(hero_name.lower().replace("_", " "))

    # get all dire heros name
    for hero in dire:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        dire_heros.append(hero_name.lower().replace("_", " "))

    # print("--- %s seconds ---" % (time.time() - start_time))

    generate_ui(radiant_heros, dire_heros)
    return radiant_heros, dire_heros
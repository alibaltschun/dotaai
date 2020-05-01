from PIL import ImageGrab
from fastai.vision import load_learner, open_image
import os
import json

BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/select_hero'
model = load_learner(MODEL_PATH)


def __split__(img):
    w, h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i*w/5, 0, (i+1)*w/5, h)))
    return r


def __read_user_data__():
    USER_DATA_DRAFTING = open(BASE + "/../django/local_data/drafting.json")
    USER_DATA_DRAFTING = USER_DATA_DRAFTING.read()
    USER_DATA_DRAFTING = json.loads(USER_DATA_DRAFTING)
    return USER_DATA_DRAFTING


def __save_user_data__(data):
    with open((BASE + "/../django/local_data/drafting.json"), 'w') as f:
        json.dump(data, f)


def update_drafting_data(radiant, dire):
    data = __read_user_data__()
    data["have_update"] = 1
    data["radiant"] = radiant
    data["dire"] = dire
    __save_user_data__(data)


def main_drafting(screen_width, screen_height, learn=model, ):
    # calculate const for crop from screenshot
    # print("get image")

    header = ImageGrab.grab((
        (screen_width*0.205),
        0,
        (screen_width-screen_width*0.205),
        screen_height-screen_height*0.93))

    screen_width, screen_height = header.size
    left = header.crop((0, 0, screen_width*.413, screen_height))
    right = header.crop((screen_width-screen_width*.413, 0,
                         screen_width, screen_height))

    radiant = __split__(left)
    dire = __split__(right)

    # set array for heros name
    radiant_heros = []
    dire_heros = []

    # temp img from model pred
    temp_file = BASE + "/../temp/select_hero.png"

    # get all radiant heros name
    for hero in radiant:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        radiant_heros.append(hero_name.replace("_", " "))

    # get all dire heros name
    for hero in dire:
        hero.save(temp_file)
        hero_name = (str(learn.predict(open_image(temp_file))[0]))
        dire_heros.append(hero_name.replace("_", " "))

    # print("--- %s seconds ---" % (time.time() - start_time))

    # generate_ui(radiant_heros, dire_heros)
    return radiant_heros, dire_heros

from PIL import ImageGrab
# import pyscreenshot as ImageGrab
from fastai.vision import load_learner, open_image
import time
import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/team'
model = load_learner(MODEL_PATH)


def pred_team(screen_width, screen_height, learn=model):

    print("get image")
    start_time = time.time()

    img = ImageGrab.grab(bbox=(
            0,
            int(screen_height-screen_height*0.225),
            int(screen_height*0.225),
            screen_height))

    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # temp img from model pred
    temp_file = BASE + "/../temp/team.png"

    print("pred team")
    img.save(temp_file)
    team = (str(learn.predict(open_image(temp_file))[0]))

    print(team)
    print("--- %s seconds ---" % (time.time() - start_time))

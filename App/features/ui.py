from PIL import ImageGrab
# import pyscreenshot as ImageGrab
from fastai.vision import load_learner, open_image
from ..utils.mp3_player import play
import time
import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/ui'
model = load_learner(MODEL_PATH)


def check_ui(screen_width, screen_height, learn=model):
    img = ImageGrab.grab((0,0,screen_height*0.15,screen_height*0.15))

    # temp img from model pred
    temp_file = BASE + "/../temp/ui.png"

    img.save(temp_file)
    ui = (str(learn.predict(open_image(temp_file))[0]))

    return ui
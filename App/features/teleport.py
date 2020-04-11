# from PIL import ImageGrab
import pyscreenshot as ImageGrab
from fastai.vision import load_learner, open_image
from ..utils.mp3_player import play
import time
import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

MODEL_PATH = BASE + '/../model/teleport'
model = load_learner(MODEL_PATH)


def check_teleport(screen_width, screen_height, learn=model):
    try:
        # calculate const for crop from screenshot
        delta_teleport = []
        if screen_width*9 > screen_height*21:
            delta_teleport.append(screen_width*.625)
            delta_teleport.append(screen_width*.666)
        else:
            delta_teleport.append(screen_width*0.66)
            delta_teleport.append(screen_width*0.74)

        print("get image")
        start_time = time.time()

        img = ImageGrab.grab(bbox=(
                int(delta_teleport[0]),
                int(screen_height*.93),
                int(delta_teleport[1]),
                int(screen_height)))

        print("--- %s seconds ---" % (time.time() - start_time))
        start_time = time.time()

        # temp img from model pred
        temp_file = BASE + "/../temp/teleport.png"

        print("pred teleport")
        img.save(temp_file)
        teleport = (str(learn.predict(open_image(temp_file))[0]))

        print(teleport)
        print("--- %s seconds ---" % (time.time() - start_time))

        return teleport

    finally:
        # TODO check user bring teleport using ai
        if teleport == "0":

            # play alert for buy teleport
            play("teleport", voice_type="alert")

# from PIL import ImageGrab
import numpy as np
import pyscreenshot as ImageGrab

from ..utils.mp3_player import play


def check_teleport(screen_width, screen_height):
    # calculate const for crop from screenshot
    delta_teleport = []
    if screen_width*9 > screen_height*21:
        delta_teleport.append(screen_width*.635)
        delta_teleport.append(screen_width*.6455)
    else:
        delta_teleport.append(screen_width*0.685)
        delta_teleport.append(screen_width*0.695)

    # get image from screen
    img = ImageGrab.grab(bbox=(
            int(delta_teleport[0]),
            int(screen_height*.97),
            int(delta_teleport[1]),
            int(screen_height*.985)))

    # count avg
    avg_teleport = np.max(np.array(img))

    print('check user bring teleport')
    # check user bring teleport
    if avg_teleport < 100:

        # play alert for buy teleport
        play("teleport", voice_type="alert")

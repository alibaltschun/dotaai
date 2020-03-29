# from PIL import ImageGrab
import pyscreenshot as ImageGrab


def get_screen_information():
    # get width and haight info from screen
    screen_width, screen_height = ImageGrab.grab().size

    return screen_width, screen_height

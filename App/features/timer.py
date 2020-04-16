from PIL import ImageGrab
# import pyscreenshot as ImageGrab
from ..utils.mp3_player import play
from ..UI.gameplay import generate_ui
from .gameplay_hero import call_heros_on_team
from .teleport import check_teleport
from PIL import ImageOps
import pytesseract

import os
BASE = (os.path.dirname(os.path.realpath(__file__)))

file_html_update = BASE + "/../temp/html_update.txt"


def update_ui():
    print("update ui")
    with open(file_html_update, "w") as file:
        file.write("1")


def check_timer(screen_width, screen_height,
                start_asistent=True, last_minutes=1,
                last_timer="0:0"):

    # calculate const for crop from screenshot
    if screen_width*9 > screen_height*21:
        delta = screen_width*0.49
    else:
        delta = screen_width*0.484

    # grab timer from screen
    timer = ImageGrab.grab((
            int(delta),
            int(screen_height*0.02),
            int(screen_width-delta),
            int(screen_height-screen_height*0.965)))

    # invert the image
    try:
        timer = ImageOps.invert(timer)

    except Exception:
        pass

    # pred the timer using ocr
    timer = pytesseract.image_to_string(
        timer,
        lang='eng',
        config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789:')

    # print the timer base on pred
    print(timer)

    # validate dota timer
    if ":" in timer:

        # call heros name while start new game
        if timer == "1:08" and last_timer == "1:09":
            generate_ui(["Welcome to the defense of the ancients"])
            update_ui()

            print("call heros name")
            call_heros_on_team(screen_width, screen_height)

        # get minutes and seconds from timer
        minutes, seconds = timer.split(":")

        # validate timer increment
        if int(seconds) > int(last_timer.split(":")[1]):

            # check player bring teleport
            if seconds == "05" or seconds == "30":
                have_teleport = check_teleport(screen_width, screen_height)
                if have_teleport == "0":
                    generate_ui(["DUDE, Buy teleport !!!"])
                    update_ui()

            # check minutes x4 or x9
            if minutes[-1:] == "4" or minutes[-1:] == "9":

                # play alert rune in 20 seconds
                if seconds == "40":
                    generate_ui(["Rune in 20 seconds"])
                    update_ui()
                    play("rune20", voice_type="alert")

                # play alert rune in 10 seconds
                elif seconds == "50":
                    generate_ui(["Rune in 10 seconds"])
                    update_ui()
                    play("rune10", voice_type="alert")

            # play alert for stacking
            elif minutes != "0" and seconds == "40":
                generate_ui(["Stack a jungle creep"])
                update_ui()
                play("stacking", voice_type="alert")

        # save last information about timer
        last_timer = timer

    return start_asistent, last_minutes, last_timer

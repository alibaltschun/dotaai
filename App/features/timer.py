# from PIL import ImageGrab
import pyscreenshot as ImageGrab
from ..utils.mp3_player import play
from .heros_name import call_heros_on_team
from .teleport import check_teleport
from PIL import ImageOps
import pytesseract


def check_timer(screen_width, screen_height,
                start_asistent=True, last_minutes=2,
                greating=True):

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

        if greating:
            call_heros_on_team(screen_width, screen_height)
            greating = False

        # get minutes and seconds from timer
        minutes, seconds = timer.split(":")
        if start_asistent:

            # check player bring teleport
            if seconds == "05" or seconds == "30":
                check_teleport(screen_width, screen_height)

            # check minutes x4 or x9
            if minutes[-1:] == "4" or minutes[-1:] == "9":

                # play alert rune in 20 seconds
                if seconds == "40":
                    play("rune20", voice_type="alert")

                # play alert rune in 10 seconds
                elif seconds == "50":
                    play("rune10", voice_type="alert")

            # play alert for stacking
            elif seconds == "45":
                play("stacking", voice_type="alert")

            # validate if play new game
            if int(minutes) < last_minutes:
                start_asistent = False

        # before 0:0
        else:

            # run assitant on minutes 1
            if int(minutes) > last_minutes:
                start_asistent = True
                greating = True
                print("start timer assistant")

            # reset last minutes
            else:
                last_minutes = int(minutes)

    return start_asistent, last_minutes, greating

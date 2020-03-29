from pygame import mixer
import os

BASE = (os.path.dirname(os.path.realpath(__file__)))

VOICE_PATH = BASE + "/../assets/voice/"
ALERT_PATH = VOICE_PATH + "alert/"
HERO_PATH = VOICE_PATH + "hero/"

mixer.init()


def play(target, voice_type):    
    # get voice path base on voice type
    if voice_type.lower() == "alert":
        PATH = ALERT_PATH

    elif voice_type.lower() == "hero":
        PATH = HERO_PATH

    # play the sound
    print("play", target + ".mp3")
    mixer.music.load(PATH + target + ".mp3")
    mixer.music.play()

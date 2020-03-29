from pygame import mixer, time
import os
from gtts import gTTS

BASE = (os.path.dirname(os.path.realpath(__file__)))

VOICE_PATH = BASE + "/../assets/voice/"
ALERT_PATH = VOICE_PATH + "alert/"
HERO_PATH = VOICE_PATH + "hero/"
COMMON_PATH = VOICE_PATH + "common/"

mixer.init()


def play_opening_game(radiant, dire):
    print("creting audio")
    radiant = ', '.join([str(x).replace("_", " ") for x in radiant])
    dire = ', '.join([str(x).replace("_", " ") for x in dire])

    tts = gTTS(""".
    welcome to the defence of the ancients.
    team radiant. {}. versus. team dire. {}.
    lets have some fun""".format(radiant, dire), lang='en')
    tts.save(VOICE_PATH + 'opening.mp3')

    # play the sound
    print("play", 'opening.mp3')
    mixer.music.load(VOICE_PATH + 'opening.mp3')
    mixer.music.play()

    # wait mixer done playing the audio
    while mixer.music.get_busy():
        time.Clock().tick(10)


def play(target, voice_type):
    # get voice path base on voice type
    if voice_type.lower() == "alert":
        PATH = ALERT_PATH

    elif voice_type.lower() == "hero":
        PATH = HERO_PATH

    elif voice_type.lower() == "common":
        PATH = COMMON_PATH

    # play the sound
    print("play", target + ".mp3")
    mixer.music.load(PATH + target + ".mp3")
    mixer.music.play()

    # wait mixer done playing the audio
    while mixer.music.get_busy():
        time.Clock().tick(10)

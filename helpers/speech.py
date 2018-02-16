#from os import system

from helpers.sub import sub
from helpers.tts import transform


def speak(text):
    assert isinstance(text, str)

    f = transform(text)
    sub(['mpg321', f])
    sub(['rm', '-f', f])

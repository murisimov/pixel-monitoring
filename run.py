import sys

from time import sleep
from PIL import Image, ImageStat
from Xlib.display import Display
from Xlib.error import BadMatch
from Xlib.X import ZPixmap

from helpers.speech import speak
from helpers.check import is_target


try:
    name = sys.argv[1]
    alert = sys.argv[2]
except IndexError:
    print("specify window name substring and alert message")
    sys.exit(66)
except Exception as e:
    print(e)
    sys.exit(1)

screen = Display().screen().root


def get_pixel_color(window, i_x, i_y):
    try:
        o_x_image = window.get_image(i_x, i_y, 1, 1, ZPixmap, 0xffffffff)
    except BadMatch:
        print("cursor is out of the window!")
        sys.exit(1)
    else:
        o_pil_image_rgb = Image.frombytes(
            "RGB", (1, 1), o_x_image.data, "raw", "BGRX"
        )
        lf_colour = ImageStat.Stat(o_pil_image_rgb).mean
        return tuple(map(int, lf_colour))


def get_window_by_name(window, content):
    if window.get_wm_name() and content in window.get_wm_name():
        return window

    for w in window.query_tree().children:
        result = get_window_by_name(w, content)
        if result:
            return result


watchable = get_window_by_name(screen, name)

color = (0, 0, 0)
x = 0
y = 0
input("press enter when cursor is at the new signature position")
while not is_target(color):
    coordinates = watchable.query_pointer()._data
    x = coordinates['win_x']
    y = coordinates['win_y']
    color = get_pixel_color(watchable, x, y)
    if not is_target(color):
        print(color)
        input("wrong position, try again")


print("watching X:%s Y:%s" % (x, y))

try:
    while True:
        current_color = get_pixel_color(watchable, x, y)
        if is_target(current_color):
            speak(alert)
            input("pixel color changed")
        sleep(1)
except (KeyboardInterrupt, SystemExit):
    print("bye")


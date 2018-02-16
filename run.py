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

deviation = 0
try:
    deviation = int(sys.argv[3])
    assert deviation < 256
except:
    pass


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

target_color = (0, 0, 0)
x = 0
y = 0
input("press enter when mouse cursor is at the target color")
while True:
    coordinates = watchable.query_pointer()._data
    x = coordinates['win_x']
    y = coordinates['win_y']
    target_color = get_pixel_color(watchable, x, y)
    answer = input("target the RGB is %s, right? (y/n)" % str(target_color))
    if answer is "y":
        break


print("watching X:%s Y:%s" % (x, y))

try:
    while True:
        current_color = get_pixel_color(watchable, x, y)
        if is_target(target_color, current_color, deviation):
            speak(alert)
            input("target color reached")
        sleep(1)
except (KeyboardInterrupt, SystemExit):
    print("\nbye")


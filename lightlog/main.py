# micro:bit v2 light logger
# Prints light level over USB serial about twice a second so the page
# can show a live "Now" value. The webpage decides how often to plot.
# The LED display is the light sensor (0-255). Button A: scroll the
# number. Button B: 1 LED per 10 light units (0-25).
from microbit import *

mode = "dots"
level = 0
last_print = 0
scroll_until = 0

def show_level(value):
    n = min(25, value // 10)
    for i in range(25):
        y = 4 - (i // 5)
        x = i % 5
        display.set_pixel(x, y, 9 if i < n else 0)

display.show(Image.YES)
sleep(400)
display.clear()

while True:
    now = running_time()
    if now - last_print >= 500:
        if mode == "dots":
            display.clear()
            sleep(20)
        level = display.read_light_level()
        print("light,{}".format(level))
        last_print = now
        if mode == "dots":
            show_level(level)
        elif now >= scroll_until:
            display.scroll(str(level), delay=80, wait=False)
            scroll_until = now + 80 * 5 * (len(str(level)) + 2)
    if button_a.was_pressed():
        mode = "text"
        scroll_until = 0
        display.scroll(str(level), delay=80, wait=False)
        scroll_until = now + 80 * 5 * (len(str(level)) + 2)
    if button_b.was_pressed():
        mode = "dots"
        scroll_until = 0
        display.clear()
        show_level(level)
    sleep(50)

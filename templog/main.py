# micro:bit v2 temperature logger
# Prints temperature over USB serial about twice a second so the page
# can show a live "Now" value. The webpage decides how often to plot.
# Button A: scroll temperature as text. Button B: 1 LED per °C (0-25).
from microbit import *

mode = "dots"
shown_text = None

def show_celsius(t):
    if t < 0:
        n = 0
    elif t > 25:
        n = 25
    else:
        n = t
    for i in range(25):
        y = 4 - (i // 5)
        x = i % 5
        display.set_pixel(x, y, 9 if i < n else 0)

display.show(Image.YES)
sleep(400)
display.clear()

while True:
    t = temperature()
    print("temp,{}".format(t))
    if button_a.was_pressed():
        mode = "text"
        shown_text = None
    if button_b.was_pressed():
        mode = "dots"
        shown_text = None
    if mode == "dots":
        show_celsius(t)
    elif t != shown_text:
        display.scroll(str(t), delay=80, wait=False, loop=True)
        shown_text = t
    sleep(500)

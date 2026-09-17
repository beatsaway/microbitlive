# micro:bit v2 temperature logger
# Prints temperature over USB serial about twice a second so the page
# can show a live "Now" value. The webpage decides how often to plot.
# Button A: scroll temperature as text. Button B: 1 LED per °C (0-25).
from microbit import *

mode = "dots"
last_print = 0
scroll_until = 0

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
    now = running_time()
    if now - last_print >= 500:
        print("temp,{}".format(t))
        last_print = now
    if button_a.was_pressed():
        mode = "text"
        scroll_until = 0
    if button_b.was_pressed():
        mode = "dots"
        scroll_until = 0
        display.clear()
    if mode == "dots":
        show_celsius(t)
    elif now >= scroll_until:
        display.scroll(str(t), delay=80, wait=False)
        scroll_until = now + 80 * 5 * (len(str(t)) + 2)
    sleep(50)

# micro:bit v2 temperature logger
# Prints temperature over USB serial about twice a second so the page
# can show a live "Now" value. The webpage decides how often to plot.
# The 5x5 LED grid is a thermometer: each lit LED is 1 °C (0-25 °C).
from microbit import *

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
    show_celsius(t)
    if button_a.was_pressed():
        display.scroll(str(t), delay=80)
        show_celsius(t)
    sleep(500)

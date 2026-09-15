# micro:bit v2 temperature logger
# Prints temperature over USB serial about twice a second so the page
# can show a live "Now" value. The webpage decides how often to plot.
from microbit import *

display.show(Image.YES)
sleep(400)
display.clear()

while True:
    t = temperature()
    print("temp,{}".format(t))
    display.set_pixel(2, 2, 9)
    sleep(50)
    display.set_pixel(2, 2, 0)
    if button_a.was_pressed():
        display.scroll(str(t), delay=80)
    sleep(450)

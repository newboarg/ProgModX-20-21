# kode til microbit som fjernstyrer bitboten

# IMPORTS
from microbit import *
import radio


# INNSTILLINGER FOR RADIO
kanal = 1  # kanal nr
radio.config(channel=kanal)
# må matche med robot, men må ikke kræsje med andre microbit/bitbotpar
radio.on()

# BILDE
display.show(Image.TRIANGLE)

# SKRIPT
while True:
    # tar inn data fra microbit
    y = int(accelerometer.get_y())  # frem / tilbake
    x = int(accelerometer.get_x())  # venstre / høyre
    a = button_a.was_pressed()
    b = button_b.was_pressed()

    control_data = [0, 0, 0, 0]
    # data som sendes til robot: [speed, tilt, button_a, button_b]
    control_data[0] = y
    control_data[1] = x

    if a:
        # knapp a (bruk defineres av robotkode)
        control_data[2] = 1
    if b:
        # knapp b (bruk defineres av robotkode)
        control_data[3] = 1
    #if not control_data[0]:
        #display.clear()
    if any(control_data):
        msg = '{}:{}:{}:{}'.format(*control_data)
        # melding som sendes til robot (type str)
        radio.send(msg)
    sleep(20)  # oppdateres hvert 20 ms
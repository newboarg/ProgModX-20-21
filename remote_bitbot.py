# kode for bit:bot

# IMPORTS
from microbit import *
import radio
import neopixel

# OPPSTART
display.show(Image.SKULL)  # logo på microbit
color = (248, 24, 148)  # NeoPixel farge for å bruke på lys
np = neopixel.NeoPixel(pin13, 12)  # variabel for neopixel

# INITIALISERING
ignition = False  # variabel for status tenning

# RADIO INNSTILLINGER
kanal = 1  # må matche med kontroller
radio.config(channel=kanal)
radio.on()


# FUNKSJONER

def move(speed, tilt):
    """Funksjon for å bevege roboten.
    Tar inn argumentene speed (int, 0-1023) og steer (int, -1023 - 1023)"""
    direction = 0
    left = 0
    right = 0
    if speed < 0:
        # fremover
        direction = 0
        left = int(min(abs(speed), 1023) * min(1, ((1023+max(-1023, 2*tilt))/1023)))
        right = int(min(abs(speed), 1023) * min(1, ((1023-min(1023, 2*tilt))/1023)))
        # print("left: %d right: %d" %(left, right))  # DEBUG
    elif speed > 0:
        # revers
        direction = 1
        left = 1023 - int(min(abs(speed), 1023) * min(1, ((1023+max(-1023, 2*tilt))/1023)))
        right = 1023 - int(min(abs(speed), 1023) * min(1, ((1023-min(1023, 2*tilt))/1023)))
        # print("left: %d right: %d" %(left, right))  # DEBUG

    # skriver til motorer
    pin8.write_digital(direction)  # retning venstre motor
    pin12.write_digital(direction)  # retning høyre motor
    pin0.write_analog(left)  # hastighet venstre motor
    pin1.write_analog(right)  # hastighet høyre motor

def honk():
    pin14.write_digital(1)
    sleep(100)
    pin14.write_digital(0)
    sleep(50)
    pin14.write_digital(1)
    sleep(100)
    pin14.write_digital(0)
    sleep(50)
    pin14.write_digital(1)
    sleep(200)
    pin14.write_digital(0)


# SKRIPT
while True:
    msg = radio.receive()
    if msg is not None:
        speed, tilt, ign, horn = [int(val) for val in msg.split(':')]
        if ign:
            print("ignition!")
            # tenning av / på
            if ignition:  # hvis tenning er på -> slå av tenning
                ignition = False
                np.clear()
            else:  # hvis tenning av -> skru på tenning
                ignition = True
                for i in range(12):
                    np[i] = color
                    np.show()  # slår på lys
                    move(0, 0)
        elif ignition:   # hvis tenning på
            move(speed, tilt)  # -> kjør robot

        if horn:
            honk()
    else:
        # hvis ikke noe beskjed fra kontroller, gjør ingenting
        move(0, 0)
    sleep(20)  # oppdater hvert 20 ms
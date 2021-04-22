from microbit import *

filename = "temperaturer.txt"
dt = 10*1000 # tid mellom målinger (i millisekunder)
stop_time = 300 * 60 * 1000 # maks tid i sekunder
t = 0
i = 0
clocks = Image.ALL_CLOCKS
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed(): # start måling
        f = open(filename, 'w')
        f.write("time(s) Temperature(C)")
        display.show(Image.TORTOISE)
        sleep(60*1000)
        break

while t <= stop_time:
    display.show(clocks[i%len(clocks)])
    f.write("\n" + str(t/1000) + " " + str(temperature()))
    t += dt
    i += 1
    sleep(dt)

f.close()
display.show(Image.SKULL)
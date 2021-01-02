# Program to blink all the LEDs in PyBoard - forever
import time
import pyb
while (1):
    for i in range(1,5):
        pyb.LED(i).toggle()
        time.sleep(1)
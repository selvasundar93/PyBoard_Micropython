from machine import Pin
p2 = Pin(2, Pin.OUT)
import time
a=1
while a==1:
    p2.on()
    time.sleep_ms(300)
    p2.off()
    time.sleep_ms(300)
from machine import Pin, PWM
import time
mg1 = Pin(12, Pin.OUT)
mg2 = Pin(25, Pin.OUT)
mg3 = Pin(4, Pin.OUT)
mg4 = Pin(18, Pin.OUT)
dil = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
while True:
    
    for s in dil ():
        mg1.value(s[0])
        mg2.value(s[1])
        mg3.value(s[2])
        mg4.value(s[3])
        time.sleep(0.005)

from machine import Pin, PWM
import time
mg1 = Pin(12, Pin.OUT)
mg2 = Pin(25, Pin.OUT)
mg3 = Pin(4, Pin.OUT)
mg4 = Pin(18, Pin.OUT)
while True:
    for i in range (1,500):
        mg1.value(1)
        mg2.value(0)
        mg3.value(0)
        mg4.value(0)
        time.sleep(0.005)
        
        mg1.value(0)
        mg2.value(1)
        mg3.value(0)
        mg4.value(0)
        time.sleep(0.005)
        
        mg1.value(0)
        mg2.value(0)
        mg3.value(1)
        mg4.value(0)
        time.sleep(0.005)
        
        mg1.value(0)
        mg2.value()
        mg3.value(0)
        mg4.value(1)
        time.sleep(0.005)

 for i in range (1, 500):
        mg1.value(0)
        mg2.value(0)
        mg3.value(0)
        mg4.value(1)
        time.sleep(0.005)
        
        mg1.value(0)
        mg2.value(0)
        mg3.value(1)
        mg4.value(0)
        time.sleep(0.005)
        
        mg1.value(0)
        mg2.value(1)
        mg3.value(0)
        mg4.value(0)
        time.sleep(0.005)
        
        mg1.value(1)
        mg2.value(0)
        mg3.value(0)
        mg4.value(0)
        time.sleep(0.005)

from machine import Pin
import time

green_led = Pin(16, Pin.OUT)
red_led = Pin(17, Pin.OUT)
blue_led = Pin(14, Pin.OUT)
yellow_led = Pin(15, Pin.OUT)

button = Pin(13, Pin.IN, Pin.PULL_UP)

total = 0

def pattern_1():
    red_led.on()
    green_led.on()
    blue_led.on()
    yellow_led.on()
    
def pattern_2():
    red_led.on()
    time.sleep(0.2)
    red_led.off()
        
    green_led.on()
    time.sleep(0.2)
    green_led.off()
        
    blue_led.on()
    time.sleep(0.2)
    blue_led.off()
        
    yellow_led.on()
    time.sleep(0.2)
    yellow_led.off()
        
def pattern_3():
    
    red_led.on()
    time.sleep(0.2)
    red_led.off()
        
    blue_led.on()
    time.sleep(0.2)
    blue_led.off()
         
    green_led.on()
    time.sleep(0.2)
    red_led.off()
        
    yellow_led.on()
    time.sleep(0.2)
    yellow_led.off()
        
    green_led.on()
    time.sleep(0.2)
    green_led.off()
        
    yellow_led.on()
    time.sleep(0.2)
    yellow_led.off()
        
    red_led.on()
    time.sleep(0.2)
    red_led.off()
        
    blue_led.on()
    time.sleep(0.2)
    blue_led.off()
        
def pattern_4():
    red_led.on()
    time.sleep(0.2)
    red_led.off()
        
    green_led.on()
    time.sleep(0.2)
    green_led.off()
        
    blue_led.on()
    time.sleep(0.2)
    blue_led.off()
        
    yellow_led.on()
    time.sleep(0.2)
    yellow_led.off()
        
        
    blue_led.on()
    time.sleep(0.2)
    blue_led.off()
        
    green_led.on()
    time.sleep(0.2)
    green_led.off()
        
    red_led.on()
    time.sleep(0.2)
    red_led.off()
        
def leds_off():
    red_led.off()
    green_led.off()
    blue_led.off()
    yellow_led.off()
        


while True:
    if button.value() == 0:
        total = total + 1
        
        if total > 4:
            total = 0
            
        print(f"The current pattern is: {total}")
        leds_off()
        
        while button.value() == 0:
            time.sleep(0.05)
        
    if total == 0:
        leds_off()
            
    elif total == 1:
        pattern_1()
            
    elif total == 2:
        pattern_2()
            
    elif total == 3:
        pattern_3()
            
    elif total == 4:
        pattern_4()

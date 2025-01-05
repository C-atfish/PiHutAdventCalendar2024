from machine import Pin
import time

redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)
onboardLED = Pin(25, Pin.OUT)
blockLED = Pin(14, Pin.OUT)

count = 0

while True:
    time.sleep(0.2)
    blockLED.value(0)
    onboardLED.value(0)
    
    if redButton.value() == 1:
        blockLED.value(1)
        count = count + 1
        print(count)  
        
    if greenButton.value() == 1:
        onboardLED.value(1)
        count = count - 1
        print(count)  
        
     
    #if redButton.value() == 1:
    #    if blockLED.value() == 1:
    #        blockLED.value(0)
    #    else:
    #        blockLED.value(1)
            
    #if greenButton.value() == 1:
    #    if onboardLED.value() == 1:
    #        onboardLED.value(0)
    #    else:
    #        onboardLED.value(1)        
from machine import Pin
import time

onboardLED = Pin(25, Pin.OUT)
blockLED = Pin(14, Pin.OUT)

while True:
    onboardLED.value(0)
    blockLED.value(0)
    time.sleep(0.5)
    print("Light on")
    blockLED.value(1)
    time.sleep(0.5)
    blockLED.value(0)
    time.sleep(0.5)
    blockLED.value(1)
    time.sleep(0.5)
    blockLED.value(0)
    time.sleep(0.5)
    onboardLED.value(1)
    time.sleep(0.5)
    onboardLED.value(0)
    time.sleep(0.5)
    onboardLED.value(1)
    blockLED.value(1)
    time.sleep(0.5)
    
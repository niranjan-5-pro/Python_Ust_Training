from machine import Pin
import utime


led = Pin(15, Pin.OUT)
while True:
  led.toggle()
  utime.sleep(0.5)
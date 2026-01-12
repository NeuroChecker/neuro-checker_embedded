from machine import Pin, ADC
from time import sleep
import math

# Initialization of ADC0
analog_pin = ADC(1)

# Initialization of GPIO21 as input
digital_pin = Pin(21,Pin.IN, Pin.PULL_UP)


print("KY-037 Microphone test")

# Endless loop for reading out the ADC
while True:
    raw_value = analog_pin.read_u16()
    # Conversion from analog value to voltage
    Volt = round(raw_value* 3.3 / 65536, 2)
    digital_pin_value = digital_pin.value()

    # Serial output of the analog value and the calculated voltage
    print("Analog voltage value: " + str(Volt) + " V\t Threshold value: ", end="")

    # Query whether the digital value has changed with serial output
    if digital_pin_value == 1:
        print("reached")
    else:
        print("not reached")
    
    sleep(2)

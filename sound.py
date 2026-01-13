from machine import Pin, ADC
from time import sleep
import math

# Initialization of ADC0
analog_pin = ADC(1)

# Initialization of GPIO21 as input
digital_pin = Pin(21,Pin.IN, Pin.PULL_UP)

# The set spanning for 1 Pa
V0 = 0.00794

# function to convert volts volts to db
def volts_to_db(Volt):
    if Volt <= 0:
        # If V is to low, then math.log will crash, because log10(0) does not exist
        return float('-inf')
    return 20 * math.log10(Volt / V0)

print("Microphone test")

# Mesureing the base on startup
print("Measuring base noise...")
sum_volt = 0
samples = 100

for _ in range(samples):
    raw_value = analog_pin.read_u16()
    V = raw * 3.3 / 65536
    sum_volt += V
    sleep(0.005)
    
base = max(sum_volt / samples, 0.01)
print("baseline", base, "V")


# Endless loop for reading out the ADC
while True:
    raw_value = analog_pin.read_u16()
    # Conversion from analog value to voltage
    Volt = raw_value * 3.3 / 65536
    
    level_db = volts_to_db(Volt)
    
    digital_pin_value = digital_pin.value()

    # Serial output of the analog value and the calculated voltage
    print("Analog voltage value: " + str(Volt) + "Threshold value: " + str(level_db), end="")

    # Query whether the digital value has changed with serial output
    if digital_pin_value == 1:
        print("reached")
    else:
        print("not reached")
    
    sleep(2)


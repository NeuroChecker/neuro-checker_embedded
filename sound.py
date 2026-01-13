from machine import Pin, ADC
from time import sleep
import math

# The set spanning for 1 Pa
V0 = 0.00794

# function to convert volts to dB
def volts_to_db(volt):
    if volt <= 0:
        # If V is too low, then math.log will crash, because log10(0) does not exist
        return float('-inf')
    return 20 * math.log10(volt / V0)

class Microphone:
    def __init__(self, analog_pin, digital_pin):
        self.adc = ADC(analog_pin)  # pinnumber 1 but will come out of main.py
        self.digital = Pin(digital_pin, Pin.IN, Pin.PULL_UP) #pinnumber will be in main.py
        self.V_max = 3.3
        self.samples = 100
        self.baseline = None
    
    def _raw_to_volt(self, raw):
        return raw * self.V_max / 65536
    
    def measure_baseline(self):
        print("Measuring base noise...")
        sum_volt = 0.0
        
        for _ in range(self.samples):
            raw_value = self.adc.read_u16()
            v = self._raw_to_volt(raw_value)
            sum_volt += v
            sleep(0.005)
            
        base = max(sum_volt / self.samples, 0.01)
        self.baseline = base
        print("Baseline:", base, "V")
        return base
    
    def read(self):
        raw = self.adc.read_u16()
        volt = self._raw_to_volt(raw)
        level_db = volts_to_db(volt)
        digital_value = self.digital.value()

        return {
            "raw": raw,
            "volt": volt,
            "db": level_db,
            "digital": digital_value,
            "baseline": self.baseline,
        }



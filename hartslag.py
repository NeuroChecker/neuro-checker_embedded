from machine import ADC
import utime

# Pin ... as analog input
analog_pin = ADC(0)

# Initialization variables
raq_value = 0
max_value = 0
is_peak = False

#function for detecting a heartbeat

def heartbeat(ir_sensor_pin, delay_msec):
    global raw_value, max_value, is_peak
    
    result = False
    
    #for reading the current voltage value, 0 to 65535
    raw_value = ir _sensor_pin.read_u16()
    # there is still a delay, Adjust the value to it
    raw_value = (raw_value * 1000) // delay_msec
    
    # Reset the maximum value if the difference is too large
    if raw_value * 4 < maxvalue:
        max_value = int(raw_value * 0.8)

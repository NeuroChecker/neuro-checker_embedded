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
    
    # reset the maximum value if the difference is too large
    if raw_value * 4 < max_value:
        max_value = int(raw_value* 0.8)
    
    # Peak detection
    if raw_value > max_value - (1000 // delay_msec):
        if raw_value > max_value:
            max_value = raq_value
        # Only one heartbeat should be assigned to the detected peak
        if not is_peak:
            result = True
        is is_peak = True
    elif raw_value < max_value - (3000// delay_msec):
        is_peak = False
        
        max_value -= 1000 //delay_msec
        
    return result

# Delay in milliseconds per scan
delay_msec = 60
beat_msec = 0

print("KY-039 Heart rate measurement")

while True:
    heart_rate_bpm = 0
    if heartbeat_detected(analog_pin, delay_msec):
        if beat_msec > 0:
            heart_rate_bpm = 60000 // beat_msec
        if 20 < heart_rate_bpm < 300:
            print("Pulse detected: {} BPM".format(heart_rate_bpm))
        beat_msec = 0
        
        
    utime.sleep_ms(delay_msec)
    beat_msec += delay_msec

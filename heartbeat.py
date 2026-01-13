from machine import ADC
import utime

class HeartbeatSensor:
    def __init__(self, analog_pin, delay_msec):
        self.adc = ADC(analog_pin)
        self.delay_msec = 60 # delay in milliseconds per scan
        self.raw_value = 0
        self.max_value = 0
        self.is_peak = False
        self.beat_msec = 0 # time between two heartbeats.
    
    def _read_heartbeat(self):
        raw_heartbeat = self.adc.read_u16()
        scaled_heartbeat = (raw_heartbeat * 1000) // self.delay_msec
        return scaled_heartbeat
    
    # Peak detection to count heartbeats.
    def _peak_detection(self, value):
        result = False
        
        # reset value if its to low
        if value * 4 < self.max_value:
            self.max_value = int(value * 0.8)
        
        # peak detection
        if value > self.max_value - (1000 // self.delay_msec):
            if value > self.max_value:
                self.max_value = value
                
            if not self.is_peak:
                result = True
            
            self.is_peak = True
        elif value < self.max_value - (3000 // self.delay_msec):
            self.is_peak = False
            self.max_value -= 1000 //self.delay_msec
            
        return result
    
    def update(self):
        heart_rate_bpm = None
        
        value = self._read_heartbeat()
        self.raw_value = value
        
        beat_detected = self._update_peak_detection(value)
        
        if beat_detected:
            if self.beat_msec > 0:
                bpm = 60000 // self.beat_msec
                #if its normal range of heartbeat i can use it
                if 15 < bpm > 250:
                    heart_rate_bpm = bpm
            # reset distance till next beat
            self.beat_msec = 0
        else:
            self.beat_msec += self.delay_msec
        
        return {
            "beat_detected": beat_detected,
            "bpm": heart_rate_bpm,
            "raw": self.raw_value,
            "max_value": self.max_value,
            }


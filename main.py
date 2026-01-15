# imports
from heartbeat import HeartbeatSensor
from time import sleep

# log function
def log(level, msg, component, extra=None):
    level_names = {
        0: "INFO",
        1: "WARN",
        2: "ERROR",
        }
    name = level_names.get(level, f"LVL{level}")
    # extra is by standerd nothing.
    extra_str = ""
    if extra:
        extra_str = " " + str(extra)
    print(f"[{name}] [{component}] {msg}")

# init_sensoren    

def init_heartbeat():
    try:
        hb = HeartbeatSensor(analog_pin=0)
        log(0, "Heartbeat sensor initialised", component="heartbeat")
        return hb
    except Exception as e:
        log(2, "Sensor Error", component="heartbeat")
        return None

# main function
def main():
    log(0, "System startup", component="main")
    # checking for faults
    hb = init_heartbeat()
    if hb is None:
        log(2, "Aborting: heartbeat not available", component="main")
        return

    log(0, "Entering main loops of components", component="main")
    # The working loop
    while True:
        data_hb = hb.update()
        if data_hb["beat_detected"] and data_hb["bpm"] is not None:
            log(
                0,
                f"Pulse detected: {data_hb['bpm']} BPM",
                component="heartbeat",
                extra={"raw": data_hb["raw"], "max": data_hb["max_value"]},
            )
        hb.sleep_until_next()

# main function used
if __name__ == "__main__":
    main()

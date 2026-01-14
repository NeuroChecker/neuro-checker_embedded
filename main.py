# imports
from time import sleep
from sound import Microphone

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

    # api connectie

# init_sensoren

def init_microphone():
    log(0, "Init microphone...", component="sound")
    
    try:
        mic = Microphone(analog_pin=1, digital_pin=21)
        base = mic.measure_baseline()
    except Exception as e:
        log(2, f"Baseline measurement failed: {e}", component="sound")
        return None

    log(0, "Baseline measured", component="sound")

    if base < 0.01 or base > 3.3:
        log(1, "Baseline out of expected range",
            component="sound")

    log(0, "Microphone init OK", component="sound")
    return mic

def main():
    log(0, "System startup")

    mic = init_microphone()
    if mic is None:
        log(2, "Aborting: microphone init failed")
        return

    log(0, "Entering main loop")

    while True:
        data_mic = mic.read()
        if data is None:
            log(1, "Mic read returned None", component="main")
        else:
            log(
                0,
                "Mic sample",
                component="sound",
                extra={
                    "volt": round(data_mic["volt"], 3),
                    "db": round(data_mic["db"], 1),
                },
            )
        sleep(2)


if __name__ == "__main__":
    main()


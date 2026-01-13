# imports


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

# main function
def main():
    log(0, "System startup")
    # checking for faults
    

    log(0, "Entering main loops of components")
    # The working loop
    

# main function used
if __name__ == "__main__":
    main()

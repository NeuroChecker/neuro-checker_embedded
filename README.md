# neuro-checker_embedded

## Guide for the ESP32-C3 Super Mini

### Introduction
This guide is meant for anyone having trouble setting up their ESP32-C3. I ran into the same issues myself and found a way to work around them.

### Step 1
Download Python 3 and run the following command:

```bash
pip install esptool
```

Check if it installed correctly by running:  
```bash
esptool.py --version
```

### Step 2
When connecting your ESP32-C3 via USB-C, make sure to hold down the **BOOT** button for about 5 seconds.

Next, open your device’s terminal and type:

```bash
esptool.py erase_flash
```

Your ESP32-C3 is now flashed and ready for any firmware you’d like to install.  
In this example, we’ll use **MicroPython**. Go to the official MicroPython website and download the correct version for your ESP32 board.

After downloading the MicroPython binary file, upload it to your ESP32 with:

```bash
esptool.py --port PORTNAME --baud 460800 write_flash 0 ESP32_BOARD_NAME-DATE-VERSION.bin
```

If the process completes successfully, your ESP32-C3 Super Mini now runs MicroPython.

***

If the last command fails, the filename might differ from the example. Run the command again, but leave everything from `ESP32` up to `.bin` blank, then press **Tab** twice to auto-complete and select the correct `.bin` file.


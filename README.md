# neuro-checker_embedded

## De handleiding voor ESP32-C3 supper mini

### inleiding
Dit is echt bedoelt voor als je een esp32-c3 hebt waar het niet goed lukt om het aan te sluiten. Ik heb hier zelf namelijk problemen mee gehad, en hierdoor heb ik het weten te omzeilen.

Stap 1
Download python 3 en voer dan deze command uit:

```pip install esptool```

Check of het gelukt is doormiddel van ```esptool.py --version```

Stap 2
Zorg dat als je de ESP32-C3 aansluit met ubs-c je ook de bootknop ingedruikt houd voor ongeveer 5 seconden.

Ga naar de terminal op je apperaat, en typ dit in:

```esptool.py erase_flash```

Nu heb je jouw ESP32-C3 geflashed en kan je er een programma naar keuze op zetten.
Zelf kies ik nu voor micro-python. ga naar de website hieronder en download micropython.

Na het downloaden van micropython kun je het op je ESP-32 zetten.

```esptool.py --port PORTNAME --baud 460800 write_flash 0 ESP32_BOARD_NAME-DATE-VERSION.bin```

Nu staat er als het gelukt is micropython op je ESP32-C3 supper mini.

-------
Als de laatste commando niet gelukt is kan het zijn dat het bestand anders is, voer de code opnieuw in, maar laat het stukje van ESP32 tot aan .bin weg en druk twee keer op tap om het juiste .bin bestand te gebruiken.



 

# Small Catch

A project for users of the raspberry pi pico w to have a small hacking pet.

## Small catch: the small fake AP

Much like a pwnagotchi, except feeding off wifi and bluetooth connections instead of handshakes. It uses a small 16x2 LCD with faces, each one conveying an action it is doing, much like a pwnagotchi. It cycles through a list of AP names, and can copy common AP names(ex: McDonald's Free WiFi).

### Hardware

- Raspberry Pi Pico W

**Link: TBA**

- 16x2 LCD Screen

**Link: TBA**

### Install guide

Navigate to the install folder

Download "RPI_PICO_W-20231005-v.21.0.uf2"

Unplug your Pico W from your computer, hold down the BOOTSEL button and plug it back into your computer while holding it down.

On your computer, navigate to the Pico's folder and drag the file you downloaded earlier into the Pico. Wait for it to install, your RPI may restart.

Make sure there is no other files in your RPI except for the core files. Download the source of Small-Catch in a zip.

Extract the zip, open the "source" folder and drag everything in the folder into the RPI's storage.

Replug your RPI in and it should be working. If it is not then please navigate to main.py, use notepad++ or any other notepad tool with a search function and search for "DEFAULT_I2C_ADDR" in the document.

Set the value to the address of your 16x2 LCD Display.

### Circuits

Display GND - > RPI Pin 38

Display VDD - > RPI Pin 40

Display SDA - > RPI Pin 1

Display SCL - > RPI Pin 2

### Emotions, and what they mean

## (^-^)

Excited, too many connections!

## (-_-)

Sleepy, eyes closed and wants to sleep. Or at least go back to sleep.

## (o_o)

Surprised, a lot of traffic may be occuring on its wifi or bluetooth connections (+10)

## (._.)

Neutral, not happy or sad. Ready to feast on user agents and connections.

## (0-0)

Happy, a connection is on its bluetooth or wifi.

## (p-p)

Crying, sad that no one wants to connect to it.

## (0o0)

Eating, its feasting on connections and user agents.

## (-O-)

Hangry, its angry because its hungry.

## (-.-)

Hungry, feed him or he will either get mad or sad.


## Connections

- ESP32 -> PI
  - PI GPIO 14 (TX) -> ESP32 RX
  - PI GPIO 15 (RX) -> ESP32 TX
  - PI GPIO 3 -> ESP32 PIN 3
  - PI GPIO 4 -> ESP32 PIN 4
  - PI GND -> ESP32 GND
- ESP32 -> SOUND SENSOR
  - ESP32 GND -> G
  - ESP32 3.3V -> +
  - ESP32 PIN 11 -> DO
- PI -> MEM I2S
  - PI 3.3V -> VCC
  - PI GND -> GND
  - PI GPIO 18 -> BCLK
  - PI GPIO 19 -> LRCLK/WS
  - PI GPIO 20 -> DATA
- ESP32 -> BUTTON

sudo systemctl restart avahi-daemon nginx

## Sleep Modes

Check your connections, genius
nmcli connection show

# Connect to the network once (manually, like the caveman you are)
nmcli dev wifi connect "YOUR_SSID" password "YOUR_PASSWORD"

# NetworkManager auto-saves it. That's literally it.
# Congratulations, you've done the bare minimum.
Verify autoconnect is actually ON (it usually is, but you're you, so let's check)
# List connections and their autoconnect status
# Try not to get confused by the column headers
nmcli -f NAME,UUID,AUTOCONNECT connection show

# If autoconnect is somehow "no" (how did you manage that?)
nmcli connection modify "YOUR_SSID" connection.autoconnect yes

 1. Light Sleep - After 5-10 minutes of silence, the PI is halted vai GPIO pin 5 command and ESP32 monitors sound. Can be woken from sleep with GPIO pin 3 and takes 3-5 seconds to turn back on again.
 2. Deep Sleep - **REQUIRES WITTY PI** With the hold of a button, the PI turns off and the ESP32 stays on tomonitor and turn it back on when it hears sound. Takes about 15-20 seconds to turn back on again.

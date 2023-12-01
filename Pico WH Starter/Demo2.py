# This is a demo of connecting to a WiFi network
# Ensure you rename secerts.py.example to secrets.py and update the values 
# to match your WiFi network
import network
import secrets
import time
wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.connect(secrets.ssid, secrets.ssid_password)

print(wlan.isconnected())
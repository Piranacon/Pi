import network
import secrets
import time
wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.connect(secrets.ssid, secrets.ssid_password)

print(wlan.isconnected())
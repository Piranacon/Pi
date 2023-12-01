import network
import secrets
import urequests
import time

wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.connect(secrets.ssid, secrets.ssid_password)

print(wlan.isconnected())


astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
print(astronauts)
numerosity = astronauts["number"]
for i in range(numerosity):
    print(astronauts["people"][i]["name"])
    print(astronauts["people"][i]["craft"])
    print("")



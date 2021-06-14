import subprocess
import paho.mqtt.client as mqtt
import time

def ping(host):
    command = ['ping', '-c', '1', host]
    return subprocess.call(command)

#host = subprocess.call(["/sbin/ip" "route|awk" "/default/ { print $3 }")
client = mqtt.Client("tester")
client.connect("172.26.0.1", port=1883, keepalive=60, bind_address="")

router = "192.168.178.1"

while True:
    client.publish("pi/con", ping(router))
    time.sleep(60)

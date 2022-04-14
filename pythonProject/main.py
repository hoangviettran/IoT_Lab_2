print("Xin chào ThingsBoard")
import paho.mqtt.client as mqttclient
import time
import json
import geocoder
import folium
import requests
import json
import random


BROKER_ADDRESS = "mqttserver.tk"
USR_NAME = "bkiot"
PASSWORD = "12345678"
TOPIC = "/bkiot/1852145/status"
PORT = 1883


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)


def connected(client, usedata, flags, rc):
    if rc == 0:
        client.subscribe(TOPIC)
        print("Connected successfully!!")
    else:
        print("Connection is failed")


client = mqttclient.Client("Gateway")
client.username_pw_set(username=USR_NAME, password=PASSWORD)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
# client.on_message = recv_message

temp = 20
humi = 50



while True:
    collect_data = {'temperature': temp, 'humidity': humi}
    temp = random.randint(0, 100)
    humi = random.randint(0, 100)
    client.publish(TOPIC, json.dumps(collect_data), 1)
    time.sleep(10)
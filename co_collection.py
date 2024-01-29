from machine import Pin, ADC
from time import sleep
import network
import json
from umqtt.robust import MQTTClient
from config import (
    WIFI_SSID, WIFI_PASS,
    MQTT_BROKER, MQTT_USER, MQTT_PASS
)

co = ADC(Pin(34))

led_wifi = Pin(2, Pin.OUT)
led_wifi.value(1)  # turn the red led off
led_iot = Pin(12, Pin.OUT)
led_iot.value(1)   # turn the green led off


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASS)
while not wlan.isconnected():
    sleep(0.5)
led_wifi.value(0)  # turn the red led on


mqtt = MQTTClient(client_id="",
                  server=MQTT_BROKER,
                  user=MQTT_USER,
                  password=MQTT_PASS)
mqtt.connect()
led_iot.value(0)   # turn the green led on


while True:
    co_ppm = co.read()/4095*1.1
    payload = {
        'lat': 13.7124,
        'lon': 100.5828,
        'co' : co_ppm}
    mqtt.publish('daq2023/group11', json.dumps(payload))
    sleep(60)
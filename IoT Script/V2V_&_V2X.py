import paho.mqtt.client as mqtt
import json
import time
import random

#MQTT broker details
broker = "broker.hivemq.com" 
#Use a public broker for testing
port = 1883
topic = "iot/automotive/v2v"
#Vehicle Data Simulator
def simulate_vehicle_data(vehicle_id):
    data = {
        "vehicle_id": vehicle_id,
        #Simulated speed in km/h
        "speed": random.randint(0, 120),
        "location": {
            "latitude": random.uniform(12.9000, 13.0000),
            "longitude": random.uniform(77.5000, 77.6000)
        },
        "timestamp": time.time()
    }
    return json.dumps(data)
#MQTT client setup
client = mqtt.Client()
client.connect(broker, port)
#Publishing vehicle data
vehicle_id = "Vehicle_1"
while True:
    vehicle_data = simulate_vehicle_data(vehicle_id)
    client.publish(topic, vehicle_data)
    print(f"Published: {vehicle_data}")
    #Publish data every 5 seconds
    time.sleep(5)
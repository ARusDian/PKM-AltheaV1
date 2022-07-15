# python 3.6
import json
import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "ALTHEATESTER/althea"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):

    data = random.randint(0, 100)
    msgData = {
        'gender': 'Laki-laki',
        'umur': 3,
        'estimasi_tinggi_badan': 80,
        'estimasi_berat_badan': 18,
        'status_gizi': 'baik',
        'lingkar_kepala': 45,
        'lingkar_lengan': 34
    }
    result = client.publish(
        topic,
        json.dumps(msgData),
        )


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
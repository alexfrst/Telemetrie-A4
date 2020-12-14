import socket, pickle
import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer
values = ["vitesse","conso"]

while True:

    UDP_IP = "0.0.0.0"
    UDP_PORT = 5004
    print("running on",UDP_IP,UDP_PORT)
    sleep(5)
    sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    sleep(10)
    producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))

    
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        data = pickle.loads(data)
        vals = {values[index] : data[index] for index in range(len(data))}
        producer.send("PE",value=vals)
        


    print("Serveur kafka introuvable réessai dans 5 seconde ")
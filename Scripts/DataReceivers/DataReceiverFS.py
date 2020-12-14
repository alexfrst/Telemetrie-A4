import socket, pickle
import sys
from time import sleep
from json import dumps
from kafka import KafkaProducer


values = ["timestamp","VR1","VR2","VR3","VR4","V","TR1","TR2","TR3","TR4","TM1","TM2","TM3","TM4","V1","V2","V3","V4","V5","V6","V7","V8","V9","VS","C1","C2","C3","C4","C5","C6","C7","C8","C9","CS","T1","T2","T3","T4","T5","T6","T7","T8","T9","TS","Long","Lat"]

while True:

    UDP_IP = "0.0.0.0"
    UDP_PORT = 5005
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
        producer.send("FS",value=vals)
        


    print("Serveur kafka introuvable réessai dans 5 secondes")
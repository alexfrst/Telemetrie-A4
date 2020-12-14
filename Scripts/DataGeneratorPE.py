label = ["vitesse","conso"]
import random, socket, pickle
from time import perf_counter, sleep


def setVoltage():
    return [random.uniform(20,30) for i in range(2)]


def sendData(sock):

    UDP_IP = "localhost"
    UDP_PORT = 5004
    values = setVoltage()
    sock.sendto(pickle.dumps(values), (UDP_IP, UDP_PORT))

def start():
    print("coucou")
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    while True:
        counter = perf_counter()
        sendData(sock)
        while counter+0.1>perf_counter(): sleep(0.01)

start()
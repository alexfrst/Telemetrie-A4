label = ["VR1","VR2","VR3","VR4","V","TM1","TM2","TM3","TM4","TR1","TR2","TR3","TR4","V1","V2","V3","V4","V5","V6","V7","V8","V9","VS","C1","C2","C3","C4","C5","C6","C7","C8","C9","CS","T1","T2","T3","T4","T5","T6","T7","T8","T9","TS","Long","Lat"]
import random, socket, pickle
from time import perf_counter, sleep

def setVitesse(speed):
    v=random.uniform(speed*0.95,speed*1.05)
    return [random.uniform(v*0.02,v*1.02),random.uniform(v*0.02,v*1.02),random.uniform(v*0.02,v*1.02),random.uniform(v*0.02,v*1.02),random.uniform(v*0.02,v*1.02)]

def setEngineTemp(temp):
    return [random.uniform(temp*0.95,temp*1.05), random.uniform(temp*0.95,temp*1.05), random.uniform(temp*0.95,temp*1.05), random.uniform(temp*0.95,temp*1.05)]

def setTorque(torque):
    v=random.uniform(torque*0.95,torque*1.05)
    return [v*(random.random()-0.5)*0.02,v*(random.random()-0.5)*0.02,v*(random.random()-0.5)*0.02,v*(random.random()-0.5)*0.02]

def setVoltage():
    return [random.uniform(4.5,6) for i in range(10)]

def setCurrent():
    return [random.uniform(0.9,1.1) for i in range(10)]

def setTemp():
    return [random.uniform(55,65) for i in range(10)]

def long():
    return [2.235784]

def lat():
    return [48.896198]

def sendData(previousVal,sock):

    UDP_IP = "localhost"
    UDP_PORT = 5005
    values = [previousVal[0]+1]+setVitesse(previousVal[5]) + setEngineTemp(previousVal[6]) +setTorque(previousVal[10]) + setVoltage() + setCurrent() + setTemp() + long() + lat()
    previousVal = values
    #print("generated:",values)
    sock.sendto(pickle.dumps(values), (UDP_IP, UDP_PORT))

def start():
    print("coucou")
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    while True:
        counter = perf_counter()
        previousVal = [0,0,0,0,0,95,70,"TM2","TM3","TM4",10,"TR2","TR3","TR4","V1","V2","V3","V4","V5","V6"
        ,"V7","V8","V9","VS","C1","C2","C3","C4","C5","C6","C7","C8","C9","CS","T1","T2","T3","T4","T5","T6","T7","T8","T9","TS","Long","Lat"]
        sendData(previousVal,sock)
        while counter+0.01>perf_counter(): sleep(0.001)

start()
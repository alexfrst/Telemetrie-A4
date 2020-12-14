from kafka import KafkaConsumer
from influxdb import InfluxDBClient
from json import loads
from time import sleep
import datetime
print("Starting")

while True:
    sleep(15)
    i = 0
    try:
        influx_client = InfluxDBClient('influxdb',8086)
        if 'telemetry' not in influx_client.get_list_database():
            influx_client.create_database('telemetry')
        influx_client.switch_database('telemetry')
    except:
        print("influxDB semble indisponible réessai dans 15s")

    consumer = KafkaConsumer(
            'FS',
            bootstrap_servers=['kafka:9093'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='FS-consumers-tel',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
    values = ["timestamp","VR1","VR2","VR3","VR4","V","TR1","TR2","TR3","TR4","TM1","TM2","TM3","TM4","V1","V2","V3","V4","V5","V6","V7","V8","V9","VS","C1","C2","C3","C4","C5","C6","C7","C8","C9","CS","T1","T2","T3","T4","T5","T6","T7","T8","T9","TS","Long","Lat"]
    print("Succesfully started and connected to kafka")
    while True:
        for event in consumer:
            i+=1
            data = event.value
            if i >= 50:
                i = 0
                json_body = [
                    {
                        "measurement":"FS",
                        "time":datetime.datetime.now().isoformat(),
                        "fields": data
                    }
                ]
                influx_client.write_points(json_body)
            

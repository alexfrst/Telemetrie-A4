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
            'PE',
            bootstrap_servers=['kafka:9093'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='PE-consumers-tel',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
    print("Succesfully started and connected to kafka")
    while True:
        for event in consumer:
            i+=1
            data = event.value
            if i >= 2:
                i = 0
                json_body = [
                    {
                        "measurement":"PE",
                        "time":datetime.datetime.now().isoformat(),
                        "fields": data
                    }
                ]
                influx_client.write_points(json_body)
            

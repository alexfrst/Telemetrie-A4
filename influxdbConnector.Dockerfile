FROM python
RUN pip install kafka-python
RUN pip install influxdb
COPY Scripts/InfluxDbConnectors/InfluxDbConnector.py InfluxDbConnector.py
COPY Scripts/InfluxDbConnectors/InfluxDbConnectorFS.py InfluxDbConnectorFS.py
COPY Scripts/InfluxDbConnectors/InfluxDbConnectorPE.py InfluxDbConnectorPE.py
CMD python -u InfluxDbConnector.py
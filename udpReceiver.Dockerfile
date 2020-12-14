FROM python
RUN pip install kafka-python
COPY Scripts/DataReceivers/DataReceiverFS.py DataReceiverFS.py
COPY Scripts/DataReceivers/DataReceiverPE.py DataReceiverPE.py
COPY Scripts/DataReceivers/DataReceiver.py DataReceiver.py
CMD python -u DataReceiver.py
FROM python:3.8-slim
RUN pip install --no-cache-dir requests
COPY . /opt/notsendgrid
CMD python /opt/notsengrid/app/request_send.py
FROM python:3.8-slim
WORKDIR /opt/notsendgrid
RUN pip install --no-cache-dir requests
COPY . .
CMD python app/request_sender.py
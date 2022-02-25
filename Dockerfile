# FROM python:3.8-slim
FROM ghashange/sendgrid-mock:1.7.2
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
# RUN update-alternatives --set python /usr/bin/python3.7
ENV SMTP_HOST="localhost"
ENV SMTP_PORT="1025"
ENV SENDGRID_MOCK_HOST="localhost"
WORKDIR /opt/notsendgrid
RUN pip install --no-cache-dir requests
COPY . .
RUN ["chmod", "+x", "/opt/notsendgrid/bin/notsendgrid_exec.sh"]
CMD ./bin/notsendgrid_exec.sh
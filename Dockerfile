# FROM python:3.8-slim
FROM golang:alpine as builder
RUN go version
RUN mkdir -p /root/gocode \
	&& export GOPATH=/root/gocode \
	&& go install github.com/mailhog/MailHog@latest
FROM ghashange/sendgrid-mock:1.7.2
COPY --from=builder /root/gocode/bin/MailHog /usr/local/bin/
WORKDIR /home/mailhog
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
# RUN update-alternatives --set python /usr/bin/python3.7
ENV SMTP_HOST="0.0.0.0"
ENV SMTP_PORT="1025"
ENV SENDGRID_MOCK_HOST="0.0.0.0"
WORKDIR /opt/notsendgrid
RUN pip install --no-cache-dir requests
COPY . .
RUN ["chmod", "+x", "/opt/notsendgrid/bin/notsendgrid_exec.sh"]
CMD ./bin/notsendgrid_exec.sh
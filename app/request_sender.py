import os
import datetime
import requests
import smtplib
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SENDGRID_MOCK_HOST = os.getenv("SENDGRID_MOCK_HOST")


def send_email(
    sender,
    receivers,
    subject,
    contents
):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receivers
    for content_type, content_body in contents:
        if content_type == "text/html":
        
            part = MIMEText(content_body, "html")

        else:

            part = MIMEText(content_body, "plain")
    
        message.attach(part)

    try:
        smtp = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
        smtp.sendmail(sender, receivers, message.as_string())         
        print("Successfully sent email")
        smtp.quit()
        return True
    except smtplib.SMTPException:
        print ("Error: unable to send email")

    return False

def request_and_send(timeout):
    
    date_time = datetime.datetime.now() - datetime.timedelta(seconds=timeout)
    date_time = date_time.isoformat()
    response = requests.get(f'http://{SENDGRID_MOCK_HOST}:3000/api/mails?dateTimeSince={date_time}')
    response = response.json()
    for email in response:

        sender = email["from"]["email"]
        subject = email["subject"]
        receivers = []
        personalizations = email["personalizations"]

        for personalization in personalizations:
            for receiver in personalization["to"]:
                receivers.append(receiver["email"])
        contents = []
        for content in email["content"]:
            content_type = content["type"]
            content_body = content["value"]
            contents.append((content_type, content_body,))

        for receiver in receivers:
            send_email(
                sender,
                receiver,
                subject,
                contents
            )


def main():

    while True:
        timeout = 5
        request_and_send(timeout)
        time.sleep(timeout)


if __name__ == "__main__":

    main()

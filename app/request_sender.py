import requests
import smtplib
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    sender,
    receivers,
    subject,
    content_type,
    content_body
):

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receivers


    if content_type == "text/html":
        
        part = MIMEText(content_body, "html")

    else:

        part = MIMEText(content_body, "plain")
    
    message.attach(part)

    try:
        smtp = smtplib.SMTP('localhost:1025')
        smtp.sendmail(sender, receivers, message.as_string())         
        print("Successfully sent email")
        smtp.quit()
        return True
    except smtplib.SMTPException:
        print ("Error: unable to send email")

    return False

def request_and_send():

    response = requests.get('https://localhost:3000/api/emails')

    for email in response:

        sender = email["from"]["email"]
        subject = email["subject"]
        receivers = []
        personalizations = email["personalizations"]

        for personalization in personalizations:
            receiever = personalization["to"]["email"]
            receivers.append(receiever)

        content_type = email["content"]["type"]
        content_body = email["content"]["value"]

        send_email(
            sender,
            receivers,
            subject,
            content_type,
            content_body
        )


def main():

    while True:
        request_and_send()
        time.sleep(5)

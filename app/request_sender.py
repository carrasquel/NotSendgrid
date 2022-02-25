import datetime
import requests
import smtplib
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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
        smtp = smtplib.SMTP(host='localhost', port=1025)
        smtp.sendmail(sender, receivers, message.as_string())         
        print("Successfully sent email")
        smtp.quit()
        return True
    except smtplib.SMTPException:
        print ("Error: unable to send email")

    return False

def request_and_send():

    response = requests.get('http://localhost:3000/api/mails')
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
        timeout = 3
        request_and_send(timeout)
        time.sleep(timeout)


if __name__ == "__main__":

    main()

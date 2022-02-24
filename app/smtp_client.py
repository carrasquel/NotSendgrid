import smtplib

sender = 'from@0.0.0.0:1030'
receivers = ['to@0.0.0.0:1025']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost:1025')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
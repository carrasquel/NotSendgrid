from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

message = Mail(
    from_email='nelson.marrero@nextroll.com',
    to_emails='tom.belote@nextroll.com',
    subject='Python link',
    html_content=html)
try:
    sg = SendGridAPIClient(api_key="unsecured_key", host="http://localhost:3000")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
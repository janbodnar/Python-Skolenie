#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['info@example.com']

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

try:
    server = smtplib.SMTP('localhost', 2500)
    # server.login('test', 'test')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print(f"Error: unable to send email: {e}")

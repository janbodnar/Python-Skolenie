#!/usr/bin/python

# python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib
from email.mime.text import MIMEText

sender = 'admin@zetcode.com'
receivers = ['info@example.com']

msg = MIMEText('Content of test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'


try:
    server = smtplib.SMTP('localhost', 1025)
    # server.login('test', 'test')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print(f"Error: unable to send email: {e}")

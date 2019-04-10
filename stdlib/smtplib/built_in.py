#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receivers = ['info@example.com']

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

port = 1025

with smtplib.SMTP('localhost', port) as server:
    
    # server.login('test', 'test')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")


# python -m smtpd -c DebuggingServer -n localhost:1025

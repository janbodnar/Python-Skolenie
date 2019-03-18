#!/usr/bin/python

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = 'admin@example.com'
receivers = ['info@example.com']

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with attachment'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

filename = 'words.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)


try:
    server = smtplib.SMTP('localhost', 2500)
    # server.login('test', 'test')
    server.sendmail(sender, receivers, msg.as_string())
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print(f"Error: unable to send email: {e}")

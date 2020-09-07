#!/usr/bin/python

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with attachment'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

filename = 'words.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

user = 'username'
password = 'password'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(username, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("Successfully sent email")
